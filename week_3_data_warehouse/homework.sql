-- SETUP
-- Create an external table using the Green Taxi Trip Records Data for 2022.
-- Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).
CREATE OR REPLACE EXTERNAL TABLE `arthur-data-engineering-course.course_dataset.external_green_taxi_data`
OPTIONS (
  format = 'parquet',
  uris = ['gs://arthur-data-engineering-course-terra-bucket/green_taxi/green_tripdata_2022-*.parquet', 'gs://arthur-data-engineering-course-terra-bucket/green_taxi/green_tripdata_2022-*.parquet']
);
---
CREATE OR REPLACE TABLE arthur-data-engineering-course.course_dataset.green_taxi_data AS
SELECT * FROM arthur-data-engineering-course.course_dataset.external_green_taxi_data;

-----

-- Question 1: What is count of records for the 2022 Green Taxi Data??
select count(1) from `arthur-data-engineering-course.course_dataset.external_green_taxi_data`
-- Answer: 840402

-- Question 2:
-- Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
-- What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?
select count(distinct(PULocationID)) from `arthur-data-engineering-course.course_dataset.external_green_taxi_data`
-- Bytes processados
-- 0 B (resultados armazenados em cache)
select count(distinct(PULocationID)) from `arthur-data-engineering-course.course_dataset.green_taxi_data`
-- Bytes processados
-- 6,41 MB

-- Question 3:
-- How many records have a fare_amount of 0?
select count(*) from `arthur-data-engineering-course.course_dataset.external_green_taxi_data`
where fare_amount = 0
-- Answer: 1622

-- Question 4:
-- What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
CREATE OR REPLACE TABLE arthur-data-engineering-course.course_dataset.green_taxi_data_optimized
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM arthur-data-engineering-course.course_dataset.external_green_taxi_data;


-- Question 5:
-- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
-- Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?
select count(distinct PULocationID) from `arthur-data-engineering-course.course_dataset.green_taxi_data`
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30';
-- Bytes processados
-- 12,82 MB
select count(distinct PULocationID) from `arthur-data-engineering-course.course_dataset.green_taxi_data_optimized`
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30';
-- Bytes processados
-- 1,12 MB
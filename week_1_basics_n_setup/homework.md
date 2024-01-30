## Homework week 1 
### Arthur Gusmão

## Question 1
`--rm`

## Question 2
Commands:
```Dockerfile
FROM python:3.9

WORKDIR /app
ENTRYPOINT [ "bash" ]
```
```bash
cd /Users/apple/Documents/data-engineering-course/week_1_basics_n_setup/docker_sql
```

```bash
docker build -t homework:v001 .
```

```bash
docker run -it homework:v001 
```
```bash
pip list
```
Result: `wheel = 0.42.0`

## Question 3
```sql
select *
from green_taxi_data
where (date(lpep_pickup_datetime) = '2019-09-18' and date(lpep_dropoff_datetime) = '2019-09-18')
order by lpep_dropoff_datetime desc
```

Result: `15612`
## Question 4

```sql
select date(lpep_pickup_datetime) as pickup_day, (lpep_dropoff_datetime - lpep_pickup_datetime) as trip_distance 
from green_taxi_data
group by 1,2 
order by 2 desc
limit 1
```

Result: `2019-09-26`

## Question 5

```sql
with table_join as (select t2."Borough",sum(t1.total_amount) as total from green_taxi_data as t1 
left join lookup_data as t2
on t1."PULocationID" = t2."LocationID"
where date(t1.lpep_pickup_datetime) = '2019-09-18' and t2."Borough" != 'Unknown'
group by 1
order by 2 desc
)
select *
from table_join
where total > 50000
```

Result: `"Brooklyn" "Manhattan" "Queens"`

## Question 6

```sql
with table_join as (
	select t1.*, t2."Zone" as pickup_zone_name
	from green_taxi_data as t1 
	left join lookup_data as t2
	on t1."PULocationID" = t2."LocationID"
	where t2."Borough" != 'Unknown'
),
table_join_2 as(
	select t1.*, t2."Zone" as dropoff_zone_name
	from table_join as t1 
	left join lookup_data as t2
	on t1."DOLocationID" = t2."LocationID"
	where t2."Borough" != 'Unknown'	

)
select dropoff_zone_name,MAX(tip_amount) 
from table_join_2
where pickup_zone_name = 'Astoria' 
group by 1
order by 2 desc
limit 1
```

Result: `JFK Airport`
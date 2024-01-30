## Homework week 1 
### Arthur Gusmão

## Question 1

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
## Question 4

```sql
select date(lpep_pickup_datetime) as pickup_day, (lpep_dropoff_datetime - lpep_pickup_datetime) as trip_distance 
from green_taxi_data
group by 1,2 
order by 2 desc
limit 1
```
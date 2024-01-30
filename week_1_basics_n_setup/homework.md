## Homework week 1 
### Arthur Gusmão

## Question 1
`--rm`

## Question 2
Commands:

Dockerfile:
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

## Question 7
Terrafomr apply output:
```bash
Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "demo_dataset"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "arthur-data-engineering-course"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "arthur-data-engineering-course-terra-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 2s [id=projects/arthur-data-engineering-course/datasets/demo_dataset]
google_storage_bucket.demo-bucket: Creation complete after 2s [id=arthur-data-engineering-course-terra-bucket]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
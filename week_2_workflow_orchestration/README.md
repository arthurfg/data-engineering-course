## Week 2 homework
#### Setup
##### Creating resources:
```bash
cd terraform
terraform plan
terraform apply
```

##### Running mage in docker and uploading parquet files to GCS:
```bash
cd ..
docker ps #check
docker compose up
```

#### Run [green_taxi_etl](https://github.com/arthurfg/data-engineering-course/blob/main/week_2_workflow_orchestration/green_taxi_etl) pipeline
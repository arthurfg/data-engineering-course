

## Week 3 homework
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
Ingesting data in gcs with mage using this [code](https://github.com/amohan601/dataengineering-zoomcamp2024/blob/main/week_3_data_warehouse/db_scripts/green_taxi_data_bigquery.sql) (from [Anju Mohan](https://github.com/amohan601) ):

```py
import io
import pandas as pd
import requests
import pyarrow.parquet as pq
import pyarrow.fs as fs
import os
from io import BytesIO
import pyarrow as pa
from urllib.parse import urlparse
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    # months = ['01']
    bucket_name = 'arthur-data-engineering-course-terra-bucket'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  "/home/src/arthur-data-engineering-course-d1fbbaefae71.json"
    project_id = kwargs.get('project_id')

    for month in months:
        file = f'green_tripdata_2022-{month}.parquet'
        print(file)
        parquet_url = base_url + file
        print(parquet_url)
        response = requests.get(parquet_url)
        df = pd.read_parquet(BytesIO(response.content))
        object_key = f'green_taxi/{file}'
        root_path = f'{bucket_name}/{object_key}'
        table = pa.Table.from_pandas(df)
        gcs = pa.fs.GcsFileSystem()
        pq.write_to_dataset(
            table,
            root_path = root_path,
            filesystem = gcs,
            use_deprecated_int96_timestamps=True
        )
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
```

#### Running SQL queries to complete the homework.
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import pyarrow as pa
import pyarrow.parquet as pq


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    bucket_name = 'arthur-data-engineering-course'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  "/home/src/arthur-data-engineering-course-d1fbbaefae71.json"
    project_id = "arthur-data-engineering-course"
    table_name = "nyc_taxi_data"
    root_path= 'f"{bucket_name}/{table_name}'
    df['tpep_pickup_date'] = df['tpep_pickup_date'].dt.date
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path,
        partition_columnns = ['tpep_pickup_date'],
        filesystem = gcs
    )
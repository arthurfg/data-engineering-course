import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
parquet_file = pq.ParquetFile("./yellow_tripdata_2023-01.parquet")

batches = parquet_file.read().to_batches(100000)
batches[0].to_pandas().head(0).to_sql(name =  "yellow_taxi_data", con = engine, if_exists = 'replace')

query2 = """
SELECT *
FROM yellow_taxi_data
LIMIT 10;
"""
print(pd.read_sql(query2, con= engine))

for batch in batches:
    start = time()
    batch.to_pandas().to_sql(name =  "yellow_taxi_data", con = engine, if_exists = 'append')
    end = time()
    print(f'batch size: {batch.num_rows}')
    print('inserted another chunk, took %.3f seconds' % (end - start))

#print(pd.io.sql.get_schema(df, name = "yellow_taxi_data", con = engine))


## Useful queries
# query = """
# SELECT *
# FROM pg_catalog.pg_tables
# WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';
# """

# query2 = """
# SELECT *
# FROM yellow_taxi_data
# LIMIT 100;
# """
# print(pd.read_sql(query2, con= engine))


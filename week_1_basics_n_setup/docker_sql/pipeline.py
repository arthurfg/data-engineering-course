import pandas as pd
from sqlalchemy import create_engine
df = pd.read_parquet("./yellow_tripdata_2023-01.parquet")

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
print(pd.io.sql.get_schema(df, name = "yellow_taxi_data", con = engine))


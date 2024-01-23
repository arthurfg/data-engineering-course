import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from urllib.parse import urlparse
from time import time
import argparse
import os

def create_table_from_parquet(parquet_file: pq.ParquetFile, table_name: str, engine: create_engine) -> None:
    """
    Create a PostgreSQL table based on the schema of a Parquet file.

    Parameters:
    - parquet_file (pq.ParquetFile): The Parquet file object.
    - table_name (str): The name for the PostgreSQL table.
    - engine (create_engine): The SQLAlchemy engine for the PostgreSQL connection.
    """
    first_batch = parquet_file.read().to_batches(100000)[0]
    first_batch.to_pandas().head(0).to_sql(name=table_name, con=engine, if_exists='replace')

def insert_into_postgres(parquet_file: pq.ParquetFile, table_name: str, engine: create_engine) -> None:
    """
    Insert data from a Parquet file into an existing PostgreSQL table in chunks.

    Parameters:
    - parquet_file (pq.ParquetFile): The Parquet file object.
    - table_name (str): The name of the PostgreSQL table.
    - engine (create_engine): The SQLAlchemy engine for the PostgreSQL connection.
    """
    batches = parquet_file.read().to_batches(100000)

    for batch in batches:
        start = time()
        batch.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')
        end = time()
        print(f'Batch size: {batch.num_rows}')
        print('Inserted another chunk, took %.3f seconds' % (end - start))

def query_postgres(query: str, engine: create_engine) -> pd.DataFrame:
    """
    Execute a SQL query on a PostgreSQL database and return the result as a Pandas DataFrame.

    Parameters:
    - query (str): The SQL query to execute.
    - engine (create_engine): The SQLAlchemy engine for the PostgreSQL connection.

    Returns:
    - pd.DataFrame: The result of the SQL query as a Pandas DataFrame.
    """
    return pd.read_sql(query, con=engine)

def main(params) -> None:
    """
    Main function to orchestrate the process of creating a table, inserting data, and querying in PostgreSQL.
    """     
    user = params.user 
    password = params.password 
    host = params.host 
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    os.system(f"curl -O {url}")
    
    path = urlparse(url).path
    parquet_file_path = f"./{os.path.basename(path)}"
    postgres_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    
    table_name = f"{table_name}"
    engine = create_engine(postgres_url)
    parquet_file = pq.ParquetFile(parquet_file_path)

    create_table_from_parquet(parquet_file, table_name, engine)

    query = """
    SELECT *
    FROM {table_name}
    LIMIT 10;
    """.format(table_name=table_name)

    result = query_postgres(query, engine)
    print(result)

    insert_into_postgres(parquet_file, table_name, engine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Ingest parquet data to Postgres')
    parser.add_argument('--user', help='Username for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='Port for Postgres')
    parser.add_argument('--db', help='Database for Postgres')
    parser.add_argument('--table_name', help='Table name for Postgres')
    parser.add_argument('--url', help='URL of parquet file')
    args = parser.parse_args()

    main(args)

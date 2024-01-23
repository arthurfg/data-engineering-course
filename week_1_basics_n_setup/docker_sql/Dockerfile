FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 pyarrow


WORKDIR /app
COPY parquet_to_postgres.py parquet_to_postgres.py
ENTRYPOINT [ "python" , "parquet_to_postgres.py"]
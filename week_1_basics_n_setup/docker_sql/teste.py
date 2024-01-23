import os 
from urllib.parse import urlparse
url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
filename = 'teste.parquet'
#os.system(f"curl -o {filename} {url}")
path = urlparse(url).path

# Obter apenas o nome do arquivo da parte final do caminho
file_name = os.path.basename(path)

print(file_name)
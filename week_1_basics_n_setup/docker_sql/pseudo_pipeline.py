import pandas as pd

colunas = [x for x in range(1,10)]
linhas = [y for y in range(1,10)]
data = {'a':colunas, 'b':  linhas}
df =pd.DataFrame(data)
print(f"DF HEAD --> {df.head()}")
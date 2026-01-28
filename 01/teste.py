import pandas as pd

print(pd.__version__)  # Isso deve mostrar a versão do pandas instalada

df = pd.read_csv('clientes.csv')  # Supondo que o arquivo esteja na mesma pasta
print(df.head())

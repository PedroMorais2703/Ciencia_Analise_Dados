import pandas as pd

df = pd.read_csv('clientes.csv')

#verificar os primeiros registros
print(df.head().to_string())

#verificar os ultimos registros
print(df.tail().to_string())

#verificar quantidade de linhas e colunas
print('quantidade', df.shape)

#verificar tipo de dados
print('tipo ', df.dtypes)

#verificar valores nulos
print('valores nulos', df.isnull().sum())
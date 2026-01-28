#analize explratoria de dados(AED)
import pandas as pd


df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')


print('Verificação inicial: ')
print(df.info())

print('Analise de dados nulos:\n', df.isnull().sum())
print('% de dados nulos: ', df.isnull().mean() * 100)
df.dropna(inplace=True)
print('confirmação da remoção de dados nulos', df.isnull().sum().sum())

print('Analize de dados duplicados', df.duplicated().sum())

print('Analize de dados unicos:', df.nunique())

print('Estatica dos dados:', df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)
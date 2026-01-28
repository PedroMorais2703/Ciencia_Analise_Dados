import pandas as pd

df = pd.read_csv("clientes.csv")

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
print(df.head())

#remover dados
df.drop('pais', axis=1, inplace=True) # remover coluna
df.drop(2, axis=0, inplace=True)# remover linha

#normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()
print(df.head())

#converter tipo de dados
df['idade'] = df['idade'].astype(int)

# tratamento de valores nulos
df_fillna = df.fillna(0) #substitui valores nulos para 0
df_dropna = df.dropna() #remove registro com valores nulos
df_dropna4 = df.dropna(thresh=4) #mantem registro com no minimo 4 valores não nulos
df = df.dropna(subset=['cpf']) # remove registros com CPF nulos

print('valores nulos:', df.isnull().sum())
print('quantidade de valores nulos com fillna:', df_fillna.isnull().sum().sum())
print('quantidade de valores nulos com dropna:', df_dropna.isnull().sum().sum())
print('quantidade de valores nulos com dropna4', df_dropna4.isnull().sum().sum())
print('quantidade de valores nulos com CPF', df.isnull().sum().sum())

df.fillna({'estado':'Desconhecido'}, inplace=True) #altera para Desonhecido
df['endereco'] = df['endereco'].fillna('Endereco não informado') #altera para endereco não informado
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # coloca a media de idade para os registros nulos

#tratar forma de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#tratando dados duplicados
print('quantidade de registros', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset=['cpf'], inplace=True)
print('quantidade de registros', len(df))

#salvar datafreme

df['idade'] = df['idade_corrigida']
df['data'] = df['data_corrigida']

df_salvar = df[['nome', 'cpf','idade','data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('novo datafreme:\n', pd.read_csv('clientes_limpeza.csv') )

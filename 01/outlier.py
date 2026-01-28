import pandas as pd
from scipy import stats

pd.set_option('display.max_columns', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] >100]
print('Filtro basico:\n', df_filtro_basico[['nome', 'idade']])

# identificador outlier com z-score
z_score = stats.zscore(df['idade'].dropna())
oultiers_z = df[z_score >= 3]
print('Outlier pelo z_score\n', oultiers_z)

#filtrando outlier com z_score
df_z_score = df[(stats.zscore(df['idade']) < 3)]

# identificador outlier com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR
print('Limite IQR:', limite_baixo, limite_alto)

outlier_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outlier IQR:', outlier_iqr)


#filtrando com IRQ
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# filtrando endereços invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço Invalido' if len(x.split(',')) < 3 else x)

#tratamento de campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome Invalido' if isinstance(x,str) and len(x) > 50 else x)
print('Quantidade de registros com numeros grandes:', (df['nome'] == "Nome Invalido").sum())

print('Dados com Outlier tratado:\n', df)

#salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

#grafico dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # scatter, hist, hex, kde, reg, resig
plt.show()

#grafico dencidade
plt.figure(figsize=[10,6])
sns.kdeplot(df['salario'], fill=True, color='blue')
plt.title('Densidade salario')
plt.xlabel('Salario')
plt.show()

# Grafico plairplot - dispesão e histograma
sns.pairplot(df[['idade','salario','anos_experiencia','nivel_educacao']])
plt.show()

#grafico regressão
sns.regplot(x='idade', y='salario', data=df, color='green', scatter_kws={'alpha':0.5,'color':'red'})
plt.title('Regressão de salario por idade')
plt.xlabel('idade')
plt.ylabel('salario')
plt.show()

#grafico countplot com hue
sns.countplot(x='idade', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('estado civil')
plt.ylabel('quantidade clientes')
plt.legend(title='Nivel educacao')
plt.show()
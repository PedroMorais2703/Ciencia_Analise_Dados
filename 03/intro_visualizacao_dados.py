import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import read_csv

df = read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())


#historograma
plt.hist(df['salario'])
plt.show()

#historograma parametro
plt.figure(figsize = (10,6))
plt.hist(df['salario'], bins = 100, color = 'green', alpha = 0.8)
plt.title('Historograma - Distribuição de Salarios')
plt.xlabel('Salario')
plt.xticks(ticks=range(0, int(df['salario'].max()) + 2000, 2000))
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

#multiplos graficos
plt.figure(figsize = (10,6))
plt.subplot(2,2,1) # 2 linhas, 2 colunas, 1ºgrafico
#grafico de dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salario e Salario')
plt.xlabel('Salario')
plt.ylabel('Salario')

plt.subplot(1,2,2)
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha = 0.6, s=30)
plt.title('Dispersão e Anos de experiencia')
plt.xlabel('Salario')
plt.ylabel('Anos de experiencia')

# mapa calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Corelação - Salario e Idade')

plt.tight_layout()
plt.show()



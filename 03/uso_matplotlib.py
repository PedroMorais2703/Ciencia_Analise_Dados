import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())


#grafico barra
plt.figure(figsize=[10,6])
df['nivel_educacao'].value_counts().plot(kind='bar', color='blue')
plt.title('Nivel de escolaridade 1')
plt.xlabel('Nivel de educacao')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=[10,6])
plt.bar(x, y, color='red')
plt.title('Nivel de escolaridade 2')
plt.xlabel('Nivel de educacao')
plt.ylabel('Quantidade')

#grafico pizza
plt.figure(figsize=[10,6])
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição do nivel de educacao')
plt.show()


#grafico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('idade')
plt.ylabel('salario')
plt.title('Dispersão de idade e salario')
plt.show()
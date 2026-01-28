import pandas as pd
import random2
from faker import Faker

faker = Faker('pt_br')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = faker.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'


    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais,
    }

    dados_pessoas.append(pessoa)

    df_pessoas = pd.DataFrame(dados_pessoas)
    print(df_pessoas)
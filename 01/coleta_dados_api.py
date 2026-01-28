import requests


def enviar_arquivos():
    # caminho do arquivo para upload
    caminho = 'C:/Users/pedro/Downloads/produtos_informatica.xlsx'

    # enviar arquivo
    requisicao = requests.post(url='https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print('arquivo enviado, link para acesso:', url)


def receber_arquivo(file_url):
    #receber arquivo
    requisicao = requests.get(file_url)

    #salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print('arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo:', requisicao.json())



receber_arquivo('https://gofile.io/d/4JvXOD')
#enviar_arquivos()
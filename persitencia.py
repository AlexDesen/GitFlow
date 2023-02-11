import json
# NA FUNÇÃO PARA CRIAR O NOME DO ARQUIVO JSON - FUNÇÃO OPEN 
# FUNÇÃO PARA REALIZAR A LEITURA DO ARQUIVO - FUNÇÃO READ 
# FUNÇAO PARA FECHA O ARQUIVO - FUNÇÃO CLOSE 
#  FUNÇÃO QUE CONVERTE O TESTO EM JSON - FUNÇÃO LOADS 
# SE NO MOMENTO DA EXECUÇÃO DER ESSE ERRO: 
# FileNotFoundError: [Errno 2] No such file or directory: 'estoque.json' 
# CRIANDO UM ARQUIVO VAZIO DE MESMO NOME RESOLVEMOS O PROBLEMA


def ler_dados_salvos():
    arquivo = open('estoque.json', 'r')
    print('Lendo dados do estoque.')
    dados_json = arquivo.read()
    arquivo.close()

    if dados_json == '':
        return []
    
    dados_python = json.loads(dados_json)
    return dados_python

    
    
        

# FUNÇÃO DUMPS - RECEBE A LISTA DE DICIONÁRIO E CRIAR UM ARQUIVO JSON REFERENTE A ESTA LISTA
# open("estoque.json , 'w'") - O 'W' PASSADO COMO ARGUMENTO INDICA
#  QUE QUEREMOS ESCREVER NO ARQUIVO, 
# SE O ARQUIVO NÃO EXISTIR O MESMO CRIA, APAGANDO O ARQUIVO ANTERIOR E SALVA UM NOVO

def salvar_dado_disco(itens_estoque):
    itens_estoque_json = json.dumps(itens_estoque)
    arquivo = open('estoque.json','w')
    arquivo.write(itens_estoque_json)
    arquivo.close()
    print('Os itens foram salvos no banco de dados.')


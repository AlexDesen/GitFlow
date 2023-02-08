 
#           TRAJETO DA GIT FLOW
#  CRIAMOS A BRANCH DEVELOP - COLOCAMOS ESTA COMO DEFAULT
# CRIAMOS AS BRANCHS DE TRABALHO
#  - CONFIGURAÇÃO_INICIAL -FUNCIONALIDADE_ADD_ESTOQUE- FUNCIONALIDADE_LISTAGEM_ITENS 
# CRIAMOS A  BRANCH DE ENTRAGA - REALESE ENTRAGA1.1.0 -
# HOUVE CORREÇÃO NO CÓDIGO  ATRAVÉS DA BRANCH - CORRECAO_CARACTERES
# O MERGER PARA A REALISE ENTREGA1.1.0
#  REALIZAMOS O MERGE DA ENTREGA1.1.0 PARA MAN 

itens_estoque = []

def adicionar_itens_estoque():   
    nome = input('Nome do iten: ')
    descricao = input('Descrição do iten: ')
    quantidade = int(input('Quantidade do iten: '))
    itens = {'nome':nome, 'descricao':descricao,'quantidade':quantidade}
    itens_estoque.append(itens)


def listar_itens_estoque():
    print('------------------------------------')
    for item in itens_estoque:
        print(f"Nome:{item['nome']}")
        print(f"Quantindade:{item['quantidade']}")
    print('------------------------------------')

if __name__ =="__main__":
    print('Sistema de estoque Ultima School\n')
    opcao = 0
    while opcao != 3:
        print('Menu de opições:')
        print(30*('='))             
        print('1 - Adicionar itens no estoque')
        print("2 - Listar itens")
        print('3 - Sair')
        opcao = int(input('Selecione uma opção: '))

        if opcao ==1:                    
            adicionar_itens_estoque()
        elif opcao == 2:
           listar_itens_estoque()
        elif opcao == 3:
            print('Obrigado por usar nosso sistema') 
        else:      
            print('Opção inválida.Tente novamente')
           
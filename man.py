
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
           
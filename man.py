if __name__ =="__main__":
    print('Sistema de estoque Ultima School\n')
    opcao = 0
    while opcao != 1:
        print('Menu de opições:')
        print(30*('='))             
        print('1 -Sair')
        opcao = int(input('Selecione uma opção: '))

        if opcao ==1:                    
            print('Obrigado por usar o nosso sistema.')
        else:
            print('Opção inválida.Tente novamente')
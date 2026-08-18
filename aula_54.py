"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    print("\n1 - Inserir | 2 - Apagar | 3 - Listar | 4 - Limpar tudo | 5 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Digite o nome de um item: ")
        lista_compras.append(item)
        print(f'{item} foi adicionado à lista!')
        
    elif opcao == "2":
        if len(lista_compras) == 0:
            print("A lista está vazia!")
            continue
        else:
            for indice, item in enumerate(lista_compras, start = 1):
                print(f"{indice}. {item}")
        
        escolha = input("Digite o número do item que deseja apagar: ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            
            if 1 <= escolha <= len(lista_compras):
                item_removido = lista_compras.pop(escolha - 1)
                print(f"{item_removido} foi removido da lista!")
            else:
                print("Esse número não existe na lista!")
        else:
            print("Digite apenas números: ")
    elif opcao == "3":
        if len(lista_compras) == 0:
            print("A lista está vazia!")
        else:
            for indice, item in enumerate(lista_compras, start = 1):
                print(f"{indice}. {item}")
    elif opcao == "4":
        if len(lista_compras) == 0:
            print("A lista já está vazia!")
            continue
        
        confirmacao = input("Tem certeza que deseja apagar todos os itens? (s/n): ")

        if confirmacao == "s":
            lista_compras.clear()
            print("Lista apagada com sucesso!")

        else:
            print("Operação cancelada.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")


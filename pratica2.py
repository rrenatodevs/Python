"""
GERENCIADOR DE ESTOQUE
Cliente gerada com IA (ClaudeAI):

👋 Olá, tudo bem?
Me indicaram você para me ajudar com um sisteminha em Python. Vou explicar o que preciso:

Tenho uma lista de produtos de uma pequena loja e preciso de um programa que funcione como 
um gerenciador de estoque simples, direto no terminal mesmo.
O programa precisa:

Cadastrar produtos com nome e quantidade em estoque
Listar todos os produtos cadastrados
Buscar um produto pelo nome
Atualizar a quantidade de um produto existente
Remover um produto da lista

Tudo isso num menu interativo, sabe? O usuário escolhe uma opção, executa a ação, e o menu 
aparece de novo até ele escolher sair.

Não precisa salvar em arquivo nem nada assim — pode ser tudo na memória mesmo, enquanto o 
programa tiver rodando.
"""

estoque = {}

def cadastrar_produto():
    nome = input("Nome do produto: ").strip().lower()

    if nome in estoque:
        print("Produto já cadastrado.")
        return
    
    try:
        quantidade = int(input("Quantidade em estoque: "))

        if quantidade < 0:
            print("Quantidade não pode ser negativo.")
            return
        
        estoque[nome] = quantidade
        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Digite uma quantidade válida.")
        

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    
    print("\n===== PRODUTOS CADASTRADOS =====")

    for nome, quantidade in estoque.items():
        print(f"Produto: {nome.title()} | Quantidade: {quantidade}")
        
        print("===============================")
        

def buscar_produto():
    nome = input("Digite o nome do produto para buscar: ").strip().lower()
    
    if nome in estoque:
        print(f"Produto encontrado: ")
        print(f"Produto: {nome.title()}")
        print(f"Quantidade: {estoque[nome]}")
    else:
        print("Produto não encontrado.")
        

def atualizar_quantidade():
    nome = input("Digite o nome do produto: ").strip().lower()
    
    if nome not in estoque: 
        print("Produto não encontrado.")
        return
    
    try:
        nova_quantidade = int(input("Nova quantidade: "))
        
        if nova_quantidade < 0:
            print("Quantidade não pode ser negativa.")
            return
        
        estoque[nome] = nova_quantidade
        print("Quantidade atualizada com sucesso!")
        
    except:
        print("Digite uma quantidade válida.")
        return
    

def remover_produto():
    nome = input("Digite o nome do produto: ").strip().lower()
    
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")
        
    
def mostrar_menu():
    print("\n===== GERENCIADOR DE ESTOQUE =====")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Atualizar quantidade")
    print("5. Remover produto")
    print("6. Sair")
    print("==================================")
    
    
# LOOP SISTEMA

while True:
    mostrar_menu()
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        cadastrar_produto()
        
    elif opcao == '2':
        listar_produtos()
        
    elif opcao == '3':
        buscar_produto()
        
    elif opcao == '4':
        atualizar_quantidade()
        
    elif opcao == '5':
        remover_produto()
        
    elif opcao == '6':
        print("Encerrando Sistema.")
        break
    
    else:
        print("Opção inválida. Por favor, tente novamente.")
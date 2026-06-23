"""
(Gerado com IA)
Oi, tudo bem? Me indicaram você como alguém que tá aprendendo programação e queria ver se consegue me ajudar com uma coisinha simples.
Eu trabalho numa lojinha e tô precisando de um programinha de cadastro de produtos — nada fancy não, só o básico mesmo.
Ele precisa:

Perguntar o nome do produto e o preço
Deixar eu cadastrar quantos produtos eu quiser (até eu falar que terminei)
No final, mostrar uma listinha com todos os produtos e os preços
E me dizer qual é o produto mais barato e o mais caro

Pode ser só no terminal mesmo, sem precisar salvar em arquivo nem nada assim.
Consegue fazer pra mim? 😊
"""

lista_de_produtos = []

while True:
    nome_do_produto = input('Digite o nome do produto (ou "sair" para terminar): ')
    if nome_do_produto.lower() == 'sair':
        break
    try:
        preco_do_produto = float(input('Digite o preço do produto: '))
        lista_de_produtos.append((nome_do_produto, preco_do_produto))
    except ValueError:
        print('Preço inválido. Por favor, digite um número.')
        continue

if lista_de_produtos:
    print('\nProdutos cadastrados:')
    for nome, preco in lista_de_produtos:
        print(f'{nome}: R$ {preco:.2f}')

    produto_mais_barato = min(lista_de_produtos, key=lambda x: x[1])
    produto_mais_caro = max(lista_de_produtos, key=lambda x: x[1])

    print(f'\nProduto mais barato: {produto_mais_barato[0]} - R$ {produto_mais_barato[1]:.2f}')
    print(f'Produto mais caro: {produto_mais_caro[0]} - R$ {produto_mais_caro[1]:.2f}')
else:
    print('Nenhum produto cadastrado.')
"""
Iterando strings com while
"""

nome = input('Digite seu nome: ')

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    print(letra)
    indice += 1

print(f'Seu novo nome é: {novo_nome}')
print(f'Seu nome tem {len(novo_nome.replace(" ", ""))} letras')
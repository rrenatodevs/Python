# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  R e n a t o
# -6-5-4-3-2-1

# nome = 'Renato'
# print(nome [2])
# print(nome [5])
# print('a' in nome)  # Verifica se a letra 'a' está presente na string 'Renato'
# print('a' not in nome)  # Verifica se a letra 'a' não está presente na string 'Renato'
# print('x' in nome)  # Verifica se a letra 'x' está presente na string 'Renato'
# print('x' not in nome)  # Verifica se a letra 'x' não está presente na string 'Renato'

nome = input('Digite seu nome: ')
encontrar = input('Digite uma letra para encontrar no seu nome: ')

if encontrar in nome:
    print(f'A letra "{encontrar}" está presente no seu nome.')
else:
    print(f'A letra "{encontrar}" não está presente no seu nome.')
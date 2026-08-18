"""
Exercício
Exiba os índices da lista

"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Renato')

indices = range(len(lista))

for i in indices:
    print(f'Índice {i}: {lista[i]}')

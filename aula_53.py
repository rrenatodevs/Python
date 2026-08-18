"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Renato')

for indice, nome in enumerate(lista):
    print(indice, nome)
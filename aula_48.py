"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis
   append = Adiciona um elemento ao final da lista
   insert = Adiciona um elemento em uma posição específica
   pop = Remove o último elemento da lista ou o elemento de uma posição específica
   del = Remove um elemento de uma posição específica
   clear = limpa a lista
   extend = Estende a lista
   + - concatena listas
Create Read Update Delete
Criar, Ler, Atualizar, Apagar = lista[i] (CRUD)
"""

lista_a = ['Renato', 'Lucas', 1, True, 1.2]
lista_b = lista_a.copy() # Cópia da lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

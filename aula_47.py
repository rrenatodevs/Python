"""
LEMBRANDO: Índices começam em 0 (ZERO)

Listas em Python
Tipo list - Mutável
Suporta várois valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, Ler, Atualizar, Deletar
"""
# ------ 0 - 1 - 2 - 3 - 5 - 6
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido', ultimo_valor)
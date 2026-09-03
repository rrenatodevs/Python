"""
Lista de listas e seus índices
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0        1        2
    ['Luiz', 'João', 'Eduarda'], #(0, 10, 20, 30, 40)], # 2
]

# print(salas[0][1]) # acessando o índice 0 que é a lista, índice 1 que é a string
# print(salas[1][0]) # acessando o índice 1 que é a lista, índice 0 que é a string
# print(salas[2][2]) # acessando o índice 2 que é a lista, índice 2 que é a string
# print(salas[2][3][3]) # acessando o índice 2 que é a lista, índice 3 que é a tupla, índice 3 que é o número dentro da tupla

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
        
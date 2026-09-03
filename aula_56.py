"""
split e join com list e str
split - divide uma string
join - une uma string

.strip() - Tira espaço do começo e do fim
.rstrip() - Tira espaço da direita
.lstrip() - Tira espaço da esquerda
"""

frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(",")  # divide a string em uma lista de palavras

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(frase.strip())  # tira espaço do começo e do fim
# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
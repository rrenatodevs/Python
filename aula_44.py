"""
Iterável -> str, range ,etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entre seu iterador
"""

texto = 'Renato' # Iterável
iterador = iter(texto) # Iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
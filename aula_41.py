frase = 'O Python é uma linguagem de programação '\
    'multiparadigm. '\
    'Python foi criado por Guido van Rossum e lançado em 1991.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_mais_frequente = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_mais_frequente = letra_atual
    
    i += 1

print(f"A letra mais frequente é {letra_mais_frequente}, "
      f"aparecendo {qtd_apareceu_mais_vezes} vezes.")
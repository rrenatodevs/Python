import unicodedata
frase = 'O Python é uma linguagem de programação '\
    'multiparadigm. '\
    'Python foi criado por Guido van Rossum e lançado em 1991.'
    
frase_normalizada = unicodedata.normalize('NFD', frase)
frase_sem_acento = ''.join(
    char for char in frase_normalizada
    if unicodedata.category(char) != 'Mn'
)

contagem = {}

for letra in frase.lower():
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
        
letra_mais_frequente = max(contagem, key=contagem.get)

print(f"A letra mais frequente é {letra_mais_frequente}, "
    f"aparecendo {contagem[letra_mais_frequente]} vezes.")

print(contagem)
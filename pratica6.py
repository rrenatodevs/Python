"""
Exercício: Sistema de Médias por Turma
Contexto

Você recebe os dados de 3 turmas de um jeito "cru" (como uma string bagunçada, do jeito que às vezes vem de um formulário ou arquivo). Sua missão é organizar tudo e calcular a média de cada turma com precisão decimal.
"""

import decimal

dados_brutos = "Maria:8.5,João:7.3,Pedro:9.1"
dados_brutos2 = "Ana:6.7,Carlos:8.8,Daniela:7.5"
dados_brutos3 = "Eduardo:9.9,Fernanda:8.0,Gustavo:7.7"

lista_dados_brutos = [dados_brutos, dados_brutos2, dados_brutos3]

turmas = []
for dados in lista_dados_brutos:
    turma_atual = []
    pedacos = dados.split(",")  # divide a string em uma lista de alunos
    for pedaco in pedacos:
        nome, nota = pedaco.split(":")
        nome = nome.strip()
        turma_atual.append((nome, nota))
    turmas.append(turma_atual)
    
medias = []
for turma in turmas:
    soma = decimal.Decimal('0')
    quantidade = 0
    for nome, nota in turma:
        soma += decimal.Decimal(nota)
        quantidade += 1
    media = soma / quantidade
    medias.append(media)
    
for i, turma in enumerate(turmas):
    nomes = [nome for nome, nota in turma]
    nomes_unidos = ', '.join(nomes)
    media_formatada = f'{medias[i]:.2f}'
    print(f'Turma {i + 1}: {nomes_unidos} - Média: {media_formatada}')
"""
Tenha uma lista de notas de alunos (você define os valores)
Use uma função (def) chamada calcular_media que recebe a lista e retorna a média
Use uma função chamada contar_aprovados que percorre a lista com for e conta quantos alunos têm nota >= 7
No final, imprima a média e quantos foram aprovados
"""

# DEF para poder calcular a média das notas dos alunos.
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    return media

# DEF para contar quantos alunos foram aprovados, ou seja, quantos têm nota >= 7. Ai somamos 1
# para cada aluno aprovado e retornamos o total de aprovados no final.
def contar_aprovados(notas):
    aprovados = 0
    for nota in notas:
        if nota >= 7:
            aprovados += 1
    return aprovados

# Programa principal para ler as notas dos alunos, calcular a média e contar os aprovados. O usuário digita
# a quantidade de alunos e as notas, que são armazenadas em uma lista. Depois, chamamos as funções
# para calcular a média e contar os aprovados, e imprimimos os resultados.
notas_alunos = []
for i in range(int(input("Digite a quantidade de alunos: "))):
    nota = int(input(f"Digite a nota do aluno {i+1}: "))
    notas_alunos.append(nota)

# Chamamos as funções para calcular a média e contar os aprovados, e imprimimos os resultados.
media = calcular_media(notas_alunos)
aprovados = contar_aprovados(notas_alunos)
print(f"A média das notas é: {media}")
print(f"A quantidade de alunos aprovados é: {aprovados}")
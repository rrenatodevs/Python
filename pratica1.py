"""
Vamos criar um programa e funções, onde
conseguimos descobrir quantas pessoas estão sendo cadastradas
e quantas pessoas são maiores de idade, e quantas são menores de idade.
"""

# primeiro vamos para a função do programa, onde vamos cadastrar as pessoas
def verificar_maiores_idade(idades):
    maiores = 0
    menores = 0
    for idade in idades:
        if idade >= 18:
            maiores += 1
        else:
            menores += 1
    return maiores, menores

# vamos contar quantas pessoas vão ser cadastradas, e depois vamos ler a idade de cada pessoa,
# armazenando as idades em uma lista. Depois, chamamos a função para verificar quantas pessoas
# são maiores de idade e quantas são menores de idade, e imprimimos os resultados.
pessoas = []
quantidade = int(input("Digite a quantidade de pessoas a serem cadastradas: "))
for i in range(quantidade):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    pessoas.append(idade)

maiores, menores = verificar_maiores_idade(pessoas)
print(f'Pessoas maiores de idade: {maiores}')
print(f'Pessoas menores de idade: {menores}')
# Variáveis são usadas para salvar algo na memória do computador, para que possamos usar esse valor mais tarde.
# PEPS: inicie variáveis com letras minúsculas, pode usar números e underline, mas não pode começar com número.
# Exemplo de criação de variáveis:
# nome = "João"
# idade = 30
# altura = 1.75
# O sinal de = é usado para atribuir um valor a uma variável. O nome da variável vem antes do sinal de = e o valor vem depois.
# Uso: nome_variavel = expressão.

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if  (idade >= 18):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
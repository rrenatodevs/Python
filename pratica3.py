"""
1. Contagem regressiva: Peça um número ao usuário e faça uma 
contagem regressiva até 0, exibindo cada valor
"""
contador = int(input("Digite um número para a contagem regressiva: "))

while contador >= 0:
    print(contador)
    contador -= 1

"""
2. Adivinhe o número: O programa define um número secreto (ex: 7).
O usuário fica tentando adivinhar em loop até acertar. A cada tentativa errada,
informe se o chute foi maior ou menor.
"""
secreto = 7

while True:
    chute = int(input("Tente adivinhar o número secreto: "))
    
    if chute == secreto:
        print("Parabéns! Você acertou!")
        break
    elif chute < secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

"""
3. Soma até parar: Fique pedindo números ao usuário e somando. O loop
só para quando ele digitar "0". No final, exiba a soma total
"""
soma = 0

while True:
    numero = int(input("Digite um número para somar (ou 0 para parar): "))

    if numero == 0:
        print(f"A soma total é: {soma}")
        break
    
    soma += numero
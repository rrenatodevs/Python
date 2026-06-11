""" Calculadora com while """

operadores_permitidos = '+-/*'

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        print("Um ou ambos os números são inválidos.")
        continue

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == '+':
        print(f"{num_1_float} + {num_2_float} = {num_1_float + num_2_float}")
    elif operador == '-':
        print(f"{num_1_float} - {num_2_float} = {num_1_float - num_2_float}")
    elif operador == '*':
        print(f"{num_1_float} * {num_2_float} = {num_1_float * num_2_float}")
    elif operador == '/':
        if num_2_float == 0:
            print("Não é possível dividir por zero.")
        else:
            print(f"{num_1_float} / {num_2_float} = {num_1_float / num_2_float}")

    if input("Quer sair? [s]im: ").lower().startswith('s'):
        break

print('Calculadora Encerrada!')
"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}.')
else:
    print('Isso não é um número inteiro.')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = int(input('Digita a hora atual (0-23): '))

try:
    
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida! Digite um número entre 0 e 23.')
except:
    print('Entrada inválida! Por favor, digite um número inteiro entre 0 e 23.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muto grande".
"""

nome = input("Digite seu primeiro nome: ")

quantidade_letras = len(nome.replace(" ", ""))

if quantidade_letras <= 4:
    print('Seu nome é curto')
elif quantidade_letras >= 5 and quantidade_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
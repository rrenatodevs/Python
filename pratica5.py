senha = '123456'
tentativas = 3

for tentativa in range(tentativas, 0, -1):
    senha_digitada = input(f'Sua senha (você tem {tentativa} tentativas): ')
    if senha_digitada == senha:
        print('Senha correta!')
        break
    elif tentativa == 1:
        print('Senha bloqueada, contatar Suporte.')
    else:
        print('Senha incorreta. Tente novamente.')
# Operadores lógicos
# and (e) or (ou) not (não)
# and: todas as expressões precisam ser verdadeiras
# Se qualquer valor for considerado (false),
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 ' ' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e')and senha_digitada == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')

# Avaliação de curto circuito
nome = 'Renato Alexandre'
altura = 1.60
peso = 60
imc = peso / (altura ** 2)
# f-strings
linha_1 = f'{nome} tem {altura} metros de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
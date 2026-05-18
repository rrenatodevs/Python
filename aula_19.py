primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

# tenta converter os dois
try:
    p = float(primeiro_valor)
    s = float(segundo_valor)
    tipo = "numero"
except ValueError:
    p = primeiro_valor.lower()
    s = segundo_valor.lower()
    tipo = "texto"

if p > s:
    print(f"Primeiro valor = '{primeiro_valor}' é maior do que o segundo valor = '{segundo_valor}'")

elif p < s:
    print(f"Segundo valor = '{segundo_valor}' é maior do que o primeiro valor = '{primeiro_valor}'")

else:
    print("Os valores são iguais")
"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754 é um padrão para representação de números reais em computadores. Ele utiliza 64 bits para armazenar um número, permitindo uma ampla gama de valores e uma precisão significativa. No entanto, devido à natureza da representação binária, nem todos os números decimais podem ser representados exatamente, o que pode levar a imprecisões em cálculos.
"""

import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal (ABCDEF0123456789)
(caractere)(> ou < ou ^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o núemro a aparecer antes dos zeros
sinal - + ou -
exemplo: 0>-100.1f
Conversion flags - !r !s !a __repr__ __str__ __ascii__
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.123456789:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')
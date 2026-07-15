"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar
a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba
    a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *;
Faça a contagem de tentativas do seu usuário e exiba quantas tentativas ele ainda tem.
"""
import os

os.system("cls" if os.name == "nt" else "clear")

palavra_secreta = "Perfume" .lower()

letras_descobertas = ["*"] * len(palavra_secreta)
tentativas = 0

print(" ".join(letras_descobertas))

while "*" in letras_descobertas:
    letras_certas = len(palavra_secreta) - letras_descobertas.count("*")
    
    if letras_certas >= 4:
        chute_palavra = input("Quer tentar chutar a palavra secreta? (S/N) ").lower()
        
        if chute_palavra == "s":
            palpite = input("Digite a palavra secreta: ").lower()
            tentativas += 1
            
            if palpite == palavra_secreta:
                letras_descobertas = list(palavra_secreta)
                continue
            else:
                print("Palavra incorreta! Vamos tentar mais uma letra")
    
    letra_chutada = input("Digite uma letra: ").lower()
    if len(letra_chutada) != 1:
        print("Por favor, digite apenas uma letra.")
        continue
    
    tentativas += 1
    encontrou = False
    
    for posicao in range(len(palavra_secreta)):
        
        if palavra_secreta[posicao] == letra_chutada:
            letras_descobertas[posicao] = letra_chutada
            encontrou = True
    
    if encontrou:
        print(f"Boa! A letra '{letra_chutada}' está na palavra secreta.")
    else:
        print(f"A letra '{letra_chutada}' não está na palavra secreta.")
    
    os.system("cls" if os.name == "nt" else "clear")

    print(" ".join(letras_descobertas))
    print(f"Tentativas: {tentativas}")
    
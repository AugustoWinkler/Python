#Desenvolver o fundamento do Jokenpo

from random import randint

jogador = int(input("""Digite o valor de sua Escolha:\n[1] Pedra:\n[2] Papel:\n[3] Tesoura:\n"""))
computador = randint(1,3)

if jogador == 1: # Jogador escolheu pedra
    if computador == 1:
        print("Empate!")
    elif computador == 2:
        print("Computador venceu!")
    else:
        print("Jogador venceu!")
elif jogador == 2: # Jogador escolheu papel
    if computador == 1:
        print("Jogador venceu!")
    elif computador == 2:
        print("Empate!")
    else:
        print("Computador venceu!")
elif jogador == 3: # Jogador escolheu tesoura
    if computador == 1:
        print("Computador venceu!")
    elif computador == 2:
        print("Jogador venceu!")
    else:
        print("Empate!")
else:
    print("Escolha inválida!")
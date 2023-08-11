import random
import json

def jogo_adivinhacao():
    #Carrega os dados dos personagens e as falas do arquivo json.
    with open('personagens.json') as json_file:
        personagens = json.load(json_file)

    personagem_escolhido = random.choice(list(personagens.keys()))
    fala_escolhida = random.choice(personagens[personagem_escolhido])

    print(f'Advinha quem disse: "{fala_escolhida}"')

    while True:
        respota = input('Digite o nome do personagem: ')

        if respota.lower() == personagem_escolhido.lower():
            print(f'Parabéns você acertou, o Personagem escolhido foi {personagem_escolhido}')
        else:
            print('Resposta incorreta, Tente novamente')
    print('O jogo acabou!')
jogo_adivinhacao()
from random import randint
for i in range(1,4):
    print(f'Nivel : {i} ({i} Casas Decimais.) ')
nivel =  int(input('Escolha o Nivel: '))
if nivel == 1:
    x = randint(0,9)
    y = randint(0, 9)
elif nivel ==2:
    x = randint(10,99)
    y = randint(10, 99)
else:
    x = randint(100,999)
    y = randint(100, 999)
while True:
    resposta = int(input(f'Quanto é {x} X {y}'))
    if resposta == x*y:
        print('Parabéns você acertou!')
        break
    else:
        print('Tente novamente:')
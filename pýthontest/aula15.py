#Break Interrompendo laços

numero = s =  0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    s+=numero
print(f'A Soma vale {s}')




### Conversão de algorismos Romanos.
### I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
### IV = 4  IX = 9, XC = 40 XD = 90 CD = 400 CM=900

numero = input('Digite um valor romano: ').upper()
resultado = 0

for c in range(len(numero)):
    for e in numero:
        print(e,c)
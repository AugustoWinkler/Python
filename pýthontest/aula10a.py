n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

n = (n1 + n2)/2

print(f'A Sua média foi {n:.2f}')

if n>=6:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim, estude mais!')
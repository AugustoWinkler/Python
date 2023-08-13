n1 = int(input('Um Valor:'))
n2 = int(input('Outro Valor:'))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Você digitou {} e {}'.format(n1 , n2))
print('a Soma entre eles é: {} \na Subtração entre eles é: {} \na Multiplicação {}\na Divisão: {:.3f}\na Divisão Inteira {}\na Exponenciação: {}'.format(s,sb,m,d,di,e))

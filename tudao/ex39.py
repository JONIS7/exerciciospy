num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print('O numero {} é maior!'.format(num1))
elif num2 > num1:
    print('O numero {} é maior'.format(num2))
else:
    print('Os dois sao iguais!')

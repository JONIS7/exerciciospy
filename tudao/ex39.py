num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))

if num1 > num2:
    print('O Primeiro numero {} é maior!'.format(num1))
elif num2 > num1:
    print('O Segundo numero {} é maior'.format(num2))
else:
    print('Os dois sao iguais!')

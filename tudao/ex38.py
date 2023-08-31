import time
num = int(input('Diga um numero qualquer: '))

conversao = int(input('''Escolha uma das bases para conversao: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opcao: '''))

print('-=-'*20)
print('                       Processando...')
print('-=-'*20)

time.sleep(2)

if conversao == 1:
    binario = bin(num)
    print('Seu numero em binario ficou >> {} <<'.format(binario)[2:])
elif conversao == 2:
    octal = oct(num)
    print('Seu numero em octal ficou >> {} <<'.format(octal)[2:])
elif conversao == 3:
    hexadecimal = hex(num)
    print('Seu numero em hexadecimal ficou >> {} <<'.format(hexadecimal)[2:])
else:
    print('Numero digitado esta incorreto!')

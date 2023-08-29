import time
num = int(input('Diga um numero qualquer: '))

print('-=-'*20)
print('                       Processando...')
print('-=-'*20)

time.sleep(2)

conversao = int(input('Digite 1 para binario, 2 para octal ou 3 para hexadecimal: '))

if conversao == 1:
    binario = bin(num)
    print('Seu numero em binario ficou >> {} <<'.format(binario))
elif conversao == 2:
    octal = oct(num)
    print('Seu numero em octal ficou >> {} <<'.format(octal))
elif conversao == 3:
    hexadecimal = hex(num)
    print('Seu numero em hexadecimal ficou >> {} <<'.format(hexadecimal))
else:
    print('Numero digitado esta incorreto!')

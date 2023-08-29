import random
from time import sleep
num_aleatorio = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5 tente advinhar....')
print('-=-'*20)

while True:
    num_usuario = int(input('Em que numero eu pensei? '))
    if 0 <= num_usuario <= 5:
        break
    else:
        print('Numeros somente de 0 a 5 por favor!')
print('PROCESSANDO....')
sleep(3)
if num_usuario == num_aleatorio:
    print('Acertou miseravel')
else:
    print('Num era esse nao mano, Eu tava pensando nesse aqui --> {} <-- nao nesse teu ai --> {} <--'.format(num_aleatorio, num_usuario))

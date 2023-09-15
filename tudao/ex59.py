import random
from time import sleep
num_aleatorio = random.randint(0,10)
num_tentativas = 0
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10 tente advinhar....')
print('-=-'*20)

while True:
    num_usuario = int(input('Em que numero eu pensei? '))
    if 0 <= num_usuario <= 10:
        break
    else:
        print('Numeros somente de 0 a 10 por favor!')
print('PROCESSANDO....')
sleep(3)
while num_usuario != num_aleatorio:
    print('Errou, eu pensei em --{}-- e vc digitou --{}--'.format(num_aleatorio, num_usuario))
    print('Tente novamente!')
    while True:
        num_usuario = int(input('Em que numero eu pensei? '))
        if 0 <= num_usuario <= 10:
            break
        else:
            print('Numeros somente de 0 a 10 por favor!')
    print('PROCESSANDO....')
    sleep(2)
    num_tentativas += 1
    if num_usuario == num_aleatorio:
        print('-=-' * 20)
        print("voce acertou pensei em --{}-- e vc mandou --{}--!".format(num_aleatorio,num_usuario))
        print("teve que tentar {} vezes pra acerta po !".format(num_tentativas))
        print('-=-' * 20)

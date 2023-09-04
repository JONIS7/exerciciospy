from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opcoes:
[ 0 ] Pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador =  int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print("PO!!")
sleep(1)
print('=-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida')

elif computador == 1:
    if jogador == 0:
        print('COMPUATDOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')



































"""import random
print('=-='*20)
print('consegue ganhar de mim no pedra papel e tesoura?')
print('                    Escolhe um:')
print('=-='*20)
ppt = str(input('Pedra, papel ou tesoura? '))

lista = ['pedra', 'papel', 'tesoura']
escolha_pc = random.choice(lista)

if ppt.lower() == 'pedra' and escolha_pc == 'papel':
    print('Eu escolhi {}, Voce perdeu haha !'.format(escolha_pc))
elif ppt.lower() == 'tesoura' and escolha_pc == 'pedra':
    print('Eu escolhi {}, Voce perdeu haha !'.format(escolha_pc))
elif ppt.lower() == 'papel' and escolha_pc == 'tesoura':
    print('Eu escolhi {}, Voce perdeu haha !'.format(escolha_pc))

elif ppt.lower() == 'papel' and escolha_pc == 'pedra':
    print('Eu escolhi {}, Voce ganhou haha !'.format(escolha_pc))
elif ppt.lower() == 'pedra' and escolha_pc == 'tesoura':
    print('Eu escolhi {}, Voce ganhou haha !'.format(escolha_pc))
elif ppt.lower() == 'tesoura' and escolha_pc == 'papel':
    print('Eu escolhi {}, Voce ganhou haha !'.format(escolha_pc))

elif ppt.lower() == escolha_pc:
    print('Eu escolhi {}, Empatamos !'.format(escolha_pc))"""



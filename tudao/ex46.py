import random
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
    print('Eu escolhi {}, Empatamos !'.format(escolha_pc))


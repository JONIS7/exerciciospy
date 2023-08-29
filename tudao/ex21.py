from random import shuffle
aluno1 = input('qual o nome do primeiro aluno? ')
aluno2 = input('e do segundo? ')
aluno3 = input('do terceiro? ')
aluno4 = input('e o ultimo aluno? ')
alunos = [aluno4, aluno3, aluno2, aluno1]
shuffle(alunos)

print('A ordem dos alunos sorteados é: ')
print(alunos)

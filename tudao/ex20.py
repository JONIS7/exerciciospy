import random
aluno1 = input('qual o nome do primeiro aluno? ')
aluno2 = input('e do segundo? ')
aluno3 = input('do terceiro? ')
aluno4 = input('e o ultimo aluno? ')
alunos = [aluno1, aluno2, aluno3, aluno4]
alunoescolhido = random.choice(alunos)
print('O aluno escolhido para vir escrever no quadro é: {}'.format(alunoescolhido))


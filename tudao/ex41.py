nota1 = float(input('Qual sua nota? '))
nota2 = float(input('Qual sua segunda nota? '))
media = (nota1 + nota2) / 2

if media > 7:
    print('O aluno tirando {:.1f} e {:.1f} a media é {:.1f}'.format(nota1, nota2, media))
    print(' Voce foi aprovado!')
elif media < 5:
    print('O aluno tirando {:.1f} e {:.1f} a media é {:.1f}'.format(nota1, nota2, media))
    print('voce foi reprovado!')
else:
    print('O aluno tirando {:.1f} e {:.1f} a media é {:.1f}'.format(nota1, nota2, media))
    print('voce esta de recuperacao!')
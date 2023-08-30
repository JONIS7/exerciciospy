nota1 = float(input('Qual sua nota? '))
nota2 = float(input('Qual sua segunda nota? '))
media = (nota1 + nota2) / 2

if media > 7:
    print('Aprovado!')
elif media < 5:
    print('Reprovado!')
else:
    print('recuperacao!')
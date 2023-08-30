ano = int(input('Qual a seu ano de nascimento? '))
idade = 2023 - ano
if idade <= 9:
    print('Mirim')
elif 10 <= idade <= 14:
    print('Infantil')
elif 15 <= idade <= 19:
    print('junior')
elif idade == 20:
    print('Senior')
else:
    print('Master')
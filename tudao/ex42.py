from datetime import date
ano = int(input('ano de nascimento? '))
data_atual =
idade = 2023 - ano
print('O atleta tem {} anos '.format(idade))
if idade <= 9:
    print('Classificacao: Mirim')
elif 10 <= idade <= 14:
    print('Classificacao: Infantil')
elif 15 <= idade <= 19:
    print('Classificacao: junior')
elif idade == 20:
    print('Classificacao: Senior')
else:
    print('Classificacao: Master')
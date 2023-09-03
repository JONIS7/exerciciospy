from datetime import date
nascimento = int(input('ano de nascimento? '))
data_atual = date.today().year
idade = data_atual - nascimento
print('O atleta tem {} anos '.format(idade))
if idade <= 9:
    print('Classificacao: Mirim')
elif idade <= 14:
    print('Classificacao: Infantil')
elif idade <= 19:
    print('Classificacao: junior')
elif idade <= 25:
    print('Classificacao: Senior')
else:
    print('Classificacao: Master')
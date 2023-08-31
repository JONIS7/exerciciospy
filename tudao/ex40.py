from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas,idade,atual))
if idade == 18:
    print('Vce tem que se alisatr imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = saldo + atual
    print('Seu alistamento é em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(saldo))
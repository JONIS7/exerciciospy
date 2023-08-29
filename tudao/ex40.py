idade = int(input('Qual seu ano de nascimento ? '))

if idade > 18:
    print('Ja se passaram {} anos da data de alistamento!'.format(idade - 18))
elif idade < 18:
    print('Ainda falta {} anos pra voce poder se alistar!'.format(18 - idade))
else:
    print('Voce esta na idade exata do alistamento militar!')

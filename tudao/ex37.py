valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o seu salario? '))
anos = float(input('Em quantos anos vc pretende pagar? '))

prestacao_maxima = salario_comprador * 0.3
meses = anos * 12

prestacaocasa = valor_casa / meses

if prestacaocasa > prestacao_maxima:
    print('Desculpe nao podemos aprovar seu emprestimo!')
else:
    print('Seu emprestimo foi aprovado, PARABENS. O valor da parcela ficou {:.2f} por {} anos!'.format(prestacaocasa,anos))

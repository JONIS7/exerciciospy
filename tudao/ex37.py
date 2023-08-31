valor_casa = float(input(' valor da casa? R$'))
salario_comprador = float(input('salario do comprador?R$ '))
anos = int(input('Em quantos anos vc pretende pagar? '))

prestacao_maxima = salario_comprador * 0.3
meses = anos * 12

prestacaocasa = valor_casa / meses

if prestacaocasa > prestacao_maxima:
    print('Para pagar a casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(valor_casa,anos,prestacaocasa))
    print('Emprestimo NEGADO')
else:
    print('Seu emprestimo foi aprovado, PARABENS. O valor da parcela ficou {:.2f} por {} anos!'.format(prestacaocasa,anos))

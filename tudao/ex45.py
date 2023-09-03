print('=' * 10, end=' ')
print('LOJAS JONIS', '=' * 10)

produto = float(input('Preço das compras: R$ '))
forma_de_pagamento = int(input('''FORMAS DE PAGAMENTO 
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] CARTÃO 1X
[ 3 ] CARTÃO 2X
[ 4 ] CARTÃO 3X OU MAIS
QUAL A OPÇÃO? '''))

if forma_de_pagamento == 1:
    total = produto - (produto * 10 / 100)
elif forma_de_pagamento == 2:
    total = produto - (produto * 5 / 100)  # Alterado de 10% para 5%
elif forma_de_pagamento == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif forma_de_pagamento == 4:
    total = produto + (produto * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))
else:
    total = produto
    print('Opção de pagamento inválida')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, total))

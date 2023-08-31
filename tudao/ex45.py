produto = float(input('Qual o preco do produto? '))
forma_de_pagamento = str(input('Qual a forma de pagamento?(avista ,cartao 1x, cartao 2x, carta 3x): '))

desconto = produto * 0.10
avista = produto - desconto

if forma_de_pagamento.lower() == 'avista':
    print('Valor do produto avista é R${:.2f}'.format(avista))
elif forma_de_pagamento.lower() == 'cartao 1x':
    desconto_cartao = produto * 0.05
    print('O valor do produto no cartao fica R${:.2f}'.format(produto - desconto_cartao))
elif forma_de_pagamento.lower() == 'cartao 2x':
    print('O valor do produto ficou por R${:.2f}'.format(produto))
elif forma_de_pagamento.lower() == 'cartao 3x':
    juros = produto * 0.20
    valor_parcelado = produto / 3
    valor_final = produto+juros
    print('Seu produto ficou por R${:.2f} com 3 parcelas de R${:.2f}'.format(valor_final, valor_parcelado))

dinheiro = int(input('me diga quantos reais tem e eu te digo quanto dolares esta valendo: '))
cot = dinheiro /3.27
valorformatado = (f'{cot:.2f}')
print('seus miseros {} estao valendo {} dolares'.format(dinheiro,valorformatado))
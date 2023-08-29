altura = float(input('qual a altura da sua parede? '))
largura = float(input('e a largura? '))
area = altura * largura
tinta = area /2
tintaformatado = f'{tinta:.1f}'
print('voce precisa de {} LITROS de tinta pra pintar sua parede.'.format(tinta))


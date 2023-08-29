numero = input('Digite um numero de 0 a 9999: ')

unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

numero = numero.zfill(4)

print('unidade:{}'.format(unidade))
print('dezena:{}'.format(dezena))
print('centena:{}'.format(centena))
print('milhar:{}'.format(milhar))
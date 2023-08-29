dis = float(input('Qual a distancia da sua viagem em kms? '))
print('Voce esta prestes a comecar uma viagem de {}kms'.format(dis))
if dis <= 200:
    valor = dis * 0.50
    print('sua viagem vai custar R${:.2f}'.format(valor))
else:
    valor2 = dis * 0.45
    print('O valor da sua viagem ficou R${:.2f} '.format(valor2))

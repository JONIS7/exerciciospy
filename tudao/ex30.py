vel = float(input('Em que velocidade esta seu carro? '))
if vel <= 80:
    print('Voce esta dentro da velocidade permitida!')
else:
    kmacima = vel - 80
    multa = kmacima * 7
    print('Voce foi multado em {} reais pelos {} kms a mais de velocidade!'.format(multa, kmacima))
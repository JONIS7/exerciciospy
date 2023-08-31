peso = float(input('Qual seu peso? '))
altura =  float(input('Qual sua altura? '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Voce esta abaixo do peso!')
elif 18.6 < imc <= 25:
    print('Voce esta no peso ideal!')
elif 26 < imc <= 30:
    print('Voce esta com sobrepeso!')
elif 30 < imc <= 40:
    print('Voce esta obeso!')
else:
    print('Voce esta com obesidade morbida!')
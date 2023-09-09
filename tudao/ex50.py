numero = int(input('me diga um numero e eu digo a tabuada dele: '))
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print('{} x {} = {}'.format(numero, multiplicador,resultado))

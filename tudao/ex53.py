numero = int(input('Digite um número: '))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print('Esse não é um número primo')
            break
    else:
        print('Este é um número primo')
else:
    print('Este não é um número primo')





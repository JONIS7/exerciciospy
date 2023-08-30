import time
print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)

r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

print('Processando....')
time.sleep(2)

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('-=-' * 20)
    print('Essas retas formam um triangulo!')
    print('-=-' * 20)

    if r1 == r2 == r3:
        print('É um triangulo equilatero')
    elif r3 == r2 or r2 == r1 or r1 == r3:
        print('é um triangulo isosceles')
    else:
        print('É um triangulo escaleno')

else:
    print('-=-' * 20)
    print('Essas retas nao formam um triangulo!')
    print('-=-' * 20)
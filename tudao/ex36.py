import time
print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)

r1 = int(input('Diga o tamanho da primeira reta: '))
r2 = int(input('Diga o tamanho da segunda reta: '))
r3 = int(input('Diga o tamanho da terceira reta: '))

print('Processando....')
time.sleep(2)

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('-=-' * 20)
    print('Essas retas formam um triangulo!')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Essas retas nao formam um triangulo!')
    print('-=-' * 20)
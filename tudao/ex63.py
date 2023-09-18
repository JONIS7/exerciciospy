primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
c = primeiro
while c <= decimo:
    print('{}'.format(c), end=' -> ')
    c += razao

mais_termos = int(input('''\nQuer ver mais termos?
[ 1 ] sim
[ 2 ] nao
qual opcao desejada? '''))
if mais_termos == 1:
    quantidade_termos = int(input('quantos termos deseja? '))

    for _ in range(quantidade_termos - 1):
        c += razao
        print('{}'.format(c), end=' -> ')
if mais_termos == 2:
    print('PROGAMA ENCERRADO!')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
c = primeiro
while c <= decimo:
    print('{}'.format(c), end=' -> ')
    c += razao
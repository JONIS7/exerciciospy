v1 = int(input('Primeiro numero: '))
v2 = int(input('Segundo numero: '))
maior = float('-inf')
res = int(input(('''                     MENU
                 [ 1 ] Somar
                 [ 2 ] Multiplicar
                 [ 3 ] Maior
                 [ 4 ] Novos numeros
                 [ 5 ] sair do progama
                 Qual vc deseja? ''')))
while res == 1:
    soma = v1 + v2
    print('O resultado da soma dos numeros é {}'.format(soma))
    break
while res == 2:
    mult = v1 * v2
    print('A multiplicacao entre os numeros é {}'.format(mult))
    break
while res == 3:
    if v1 > v2:
        maior = v1
        print('O maior numero é {}'.format(maior))
    if v2 > v1:
        maior = v2
        print('O maior numero é {}'.format(maior))
    if v1 == v2:
        print('Eles sao iguais')
    break
while res == 4:
    v1 = int(input('Primeiro numero: '))
    v2 = int(input('Segundo numero: '))
    maior = float('-inf')
    res = int(input(('''                     MENU
                     [ 1 ] Somar
                     [ 2 ] Multiplicar
                     [ 3 ] Maior
                     [ 4 ] Novos numeros
                     [ 5 ] sair do progama
                     Qual vc deseja? ''')))
    while res == 1:
        soma = v1 + v2
        print('O resultado da soma dos numeros é {}'.format(soma))
        break
    while res == 1:
        mult = v1 * v2
        print('A multiplicacao entre os numeros é {}'.format(mult))
        break
    while res == 3:
        if v1 > v2:
            maior = v1
        if v2 > v1:
            maior = v2
        print('O maior numero é {}'.format(maior))
        break
while res == 5:
    print('Progama finalizado!')
    break
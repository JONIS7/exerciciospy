num = int(input('Digite um numero: '))
lista_num = []
num_digitados = 0
maior_num = float('-inf')
menor_num = float('inf')

while num != 10000000000:
    lista_num.append(num)
    num_digitados += 1
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num
    continuar = str(input('Deseja continuar [S/N]: ')).strip()
    if continuar.upper() == 'S':
        num = int(input('Digite um numero: '))
    else:
        print('PROGAMA FINALIZADO')
        break
soma = sum(lista_num)
media = soma / num_digitados
print('A media entre os numeros {:.2f}'.format(media))
print('O maior numero é {}'.format(maior_num))
print('O menor numero é {}'.format(menor_num))

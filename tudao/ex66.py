num = int(input('Digite um numero: '))
lista_num = []
maior_num = float('-inf')
menor_num = float('inf')

while num != 999:
    lista_num.append(num)
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num
    media = 
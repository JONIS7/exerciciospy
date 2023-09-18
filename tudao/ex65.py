num = int(input('Digite um numero: '))
num_digitados = 0
total_num = []

while num != 999:
    num_digitados += 1
    total_num.append(num)
    num = int(input('Digite um numero: '))
soma = sum(total_num)

print('Foram digitados {} numeros e a soma entre eles é {} '.format(num_digitados,soma))
print(total_num)


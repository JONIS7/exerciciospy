num = int(input('Digite um numero:' ))
if num < 0:
    print('Fatorial nao funciona com numeros negativos')
else:
    resultado = 1
    contador = 1
while contador <= num:
    resultado *= contador
    contador += 1
print('O fatorial de {} é {} '.format(num, resultado))

'''def is_palindrome(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]
frase =(input('Digite uma frase: '))
if is_palindrome(frase):
    print('A frase é um palindromo')
else:
    print('A frase nao é um palindromo')'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letraa in range(len(junto) -1, -1, -1):
    inverso += junto[letraa]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao é um palindromo')



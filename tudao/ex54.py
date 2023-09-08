def is_palindrome(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]
frase =(input('Digite uma frase: '))
if is_palindrome(frase):
    print('A frase é um palindromo')
else:
    print('A frase nao é um palindromo')


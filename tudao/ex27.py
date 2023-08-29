frase = str(input('Digite uma frase de efeito: ')).strip().upper()

print('A letra "A" aparece {} vezes '.format(frase.count('A')))
print('Ela aparece pela primeira vez {}'.format(frase.find('A')+1))
print('E vemos ela pela ultima vez na posicao {}'.format(frase.rfind('A')+1))
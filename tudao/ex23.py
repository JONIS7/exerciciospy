nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome completo em maiusculo é {}'.format(nome.upper()))
print('Seu nome completo minusculo é {}'.format(nome.lower()))
print('O total de letras no seu nome é: {} '.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem um total de {} letras'.format(nome.find(' ')))

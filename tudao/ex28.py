nome_completo = input('Qual seu nome completo: ').strip()

parte_do_nome = nome_completo.split()
primeiro = parte_do_nome[0]
ultimo = parte_do_nome[-1]

print('Seu nome completo é {}'.format(nome_completo))
print('seu primeiro nome é {}'.format(primeiro))
print('seu ultimo nome é {}'.format(ultimo))
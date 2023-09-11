
maiores = 0
menores = 0


for c in range(1, 8):
    nas = int(input('({}) Qual seu ano de nascimento: '.format(c)))
    maioridade = 2023 - nas
    if maioridade > 18:
        maiores += 1
    else:
        menores += 1


print('{} dessas pessoas são maiores de idade \nE {} são menores de idade'.format(maiores, menores))

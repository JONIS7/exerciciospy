idades = []
h_mais_velho_nome = None
h_mais_velho_idade = float('-inf')
mulheres_menoresde20 = 0

for c in range(4):
    nome = input('Qual seu nome: ')
    idade = int(input('Qual sua idade: '))
    sexo = input('Qual seu sexo (M/F): ')
    print('PROXIMO!')

    idades.append(idade)

    if sexo.upper() == 'M' and idade > h_mais_velho_idade:
        h_mais_velho_idade = idade
        h_mais_velho_nome = nome

    if sexo.upper() == 'F' and idade < 20:
        mulheres_menoresde20 += 1

media_idade = sum(idades) / 4

print('A média de idade das pessoas é: {:.2f}'.format(media_idade))
if h_mais_velho_nome:
    print('O homem mais velho é:', h_mais_velho_nome)
else:
    print('Não há homens na lista.')

print('O número de mulheres com menos de 20 anos é:', mulheres_menoresde20)




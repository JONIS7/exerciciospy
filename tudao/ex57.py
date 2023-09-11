idades = []
h_mais_velho_nome = None
h_mais_velho_idade = float('-inf')
mulheres_menoresde20 = 0

for c in range(1 , 5):
    print('----- {}* PESSOA ----- '.format(c))
    nome = str(input('Qual seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = input('Qual seu sexo (M/F): ').strip()
    print('PROXIMO!')

    idades.append(idade)

    if sexo.upper() == 'M' and idade > h_mais_velho_idade:
        h_mais_velho_idade = idade
        h_mais_velho_nome = nome

    if sexo.upper() == 'F' and idade < 20:
        mulheres_menoresde20 += 1

media_idade = sum(idades) / 4

print('A média de idade das pessoas é{:.1f} anos'.format(media_idade))
if h_mais_velho_nome:
    print('O homem mais velho tem {} anos e se chama {}'.format(h_mais_velho_idade, h_mais_velho_nome))
else:
    print('Não há homens na lista.')

print('Ao todo sao {} mulheres com menos de 20 anos'.format(mulheres_menoresde20))




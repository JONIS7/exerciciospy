maiorp = float('-inf')
menorp = float('inf')

for c in range(5):
    peso = float(input('Qual seu peso: '))
    if peso > maiorp:
        maiorp = peso
    if peso < menorp:
        menorp = peso

print( 'O maior peso é {:.1f} Kgs e o menor é {:.1f} kgs'.format(maiorp, menorp))

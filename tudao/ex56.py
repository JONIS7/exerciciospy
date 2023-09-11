maiorp = float('-inf')
menorp = float('inf')

for c in range(1, 6):
    peso = float(input('({}) Qual seu peso: '.format(c)))
    if peso > maiorp:
        maiorp = peso
    if peso < menorp:
        menorp = peso

print( 'O maior peso é {:.1f} Kgs\nE o menor é {:.1f} kgs'.format(maiorp, menorp))

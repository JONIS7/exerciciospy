salario = float(input('Qual o seu salario? R$'))
if salario > 1250:
    conta = salario*10/100
    aumento10 = conta + salario
    print(f'Seu salario aumentou em 10% ficando {aumento10} Reais')
else:
    conta2 = salario*15/100
    aumento2 = salario + conta2
    print(f'Seu salario recebeu aumento de 15% ficando {aumento2} Reais')

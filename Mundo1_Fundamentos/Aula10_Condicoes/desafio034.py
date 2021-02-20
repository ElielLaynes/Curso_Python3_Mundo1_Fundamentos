
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

    # Para salários ACIMA de R$ 1.250,00, calcule aumento de 10%

    # Para salários ABAIXO de R$ 1.250,00, calcule aumento de 15%


salario = float ( input('Qual é o seu Salário atual? R$:  '))

aumento10 = salario + (salario * 0.10)
aumento15 = salario + (salario * 0.15)

if salario >= 1.250:
    print(f'Se novo salário a partir do próximo mês será de: R$ {aumento10}')
else:
    print(f'Seu salário a parit do próximo mês será de: R$ {aumento15}')
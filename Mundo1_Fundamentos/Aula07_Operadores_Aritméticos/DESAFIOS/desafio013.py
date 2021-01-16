# Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de Aumento.

salario_atual = float(input('Qual é o seu salário atual? '))
aumento = salario_atual * 0.15
salario_atualizado = salario_atual + aumento
print('Seu Salário atual é de R${:.2f} reais'.format(salario_atual))
print('Com aumento de 15%, seu novo salário é de R${} reais'.format(salario_atualizado))
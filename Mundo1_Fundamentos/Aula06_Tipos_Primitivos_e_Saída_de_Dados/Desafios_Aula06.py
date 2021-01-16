# Desafio 004
# Crie um program que leia dois números e mostre a soma entre eles.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
'''

# Faça um programa que leia algo pelo treclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

info = input('Digite alguma coisa: ')
print('O tipo primitivo é ', type(info))
print('é alfabético',info.isalpha())
print('é maiscula',info.isupper())
print('é numérico', info.isnumeric())
print('é minuscula', info.islower())
print('é printável', info.isprintable())
print('tem espaço', info.isspace())

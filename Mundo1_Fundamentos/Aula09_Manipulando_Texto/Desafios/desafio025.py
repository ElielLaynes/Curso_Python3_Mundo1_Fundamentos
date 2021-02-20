# Crie um programa que leia o nome de uma pessoa e difa se ela tem 'SILVA' no nome.

print('=*' * 50)

nome = str(input('Digite seu nome: '))

if 'Silva' in nome:
    print('Seu nome TEM Silva')
else:
    print('Seu nome NÃO TEM Silva')
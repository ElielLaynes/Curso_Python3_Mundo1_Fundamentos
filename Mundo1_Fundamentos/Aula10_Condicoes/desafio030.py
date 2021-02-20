# Crei um programa que:

    # leia um número inteiro
    # mostre na tela se ele é PAR
    # Mostre na tela se ele é IMPAR

print()
print('É PAR ou ÍMPAR?')
print()

numero = int(input('Digite um Número: '))

# Opção 1
if numero % (2 == 0):
    print('PAR')
else:
    print('IMPAR')

# Opção 2
if numero % (2 != 0):
    print('IMPAR')
else:
    print('PAR')


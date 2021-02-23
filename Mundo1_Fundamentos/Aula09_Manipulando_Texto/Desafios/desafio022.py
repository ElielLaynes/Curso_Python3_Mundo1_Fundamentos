# Crie um programa que leio o nome completo de uma pessoa e mostre:
    # O nome com toads as letras MAIÚSCULAS
    # O nome com todas as letras minúsculas
    # Quantas letras tem o nome ao todo (sem considerar os espaços)
    # Quantas letras tem o primeiro nome.

print()
nome = str(input('Digite sue nome: '))

ma = nome.upper()
mi = nome.lower()

nome_div = nome.split()
nome_jun = ''.join(nome)

tam = len(nome_jun)
tamp = len(nome_div[0])

print(f'\nO nome digitado foi : {nome}\n')
print(f'Seu nome com letras Maiúsculas é: {ma}\n')
print(f'Seu nome com letras Minúsculas é: {mi}\n')
print(f'Seu nome tem ao todo: {tam} letras\n')
print(f'Seu primeiro nome tem {tamp} letras')

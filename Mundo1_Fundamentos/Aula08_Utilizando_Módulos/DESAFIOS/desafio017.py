# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento e hipotenusa.

# Importando a biblioteca math
from math import hypot

# Desafio 017
cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
catedo_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hypotenusa = hypot(cateto_oposto, catedo_adjacente)
print(f'O comprimento da Hypotenusa é: {hypotenusa:.3f}')

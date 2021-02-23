# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo


# Importando a bibloteca math
from math import sin, cos, tan


# Desafio 018

angulo = float(input('Digite um Ângulo: '))

sen = sin(angulo)
cos = cos(angulo)
tan = tan(angulo)

print(f'O Seno vale: {sen:.3f}\nCosseno: {cos:.2f}\nTangente: {tan}')

# Escreva um programa que converta uma temperatura digita em graus Celsius e converta para  Fahrenheit

temperatura = float(input('Qual a temperatura no momento? '))
conversao = (temperatura * 9/5) + 32
print('A temperatura de {} C, corresponde a {} F!'.format(temperatura, conversao))
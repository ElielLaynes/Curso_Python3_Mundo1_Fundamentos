# Crie um programa que leia uma número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: 
       # Digite um número: 6.127
       # O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um Número Real qualquer: '))
print('O número {} tem a parte inteira {}'. format(num, trunc(num)))
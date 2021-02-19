# Crie um programa que leia uma número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: 
       # Digite um número: 6.127
       # O número 6.127 tem a parte inteira 6.

# importando a biblioteca math e usando o médoto trunc (truncate)
from math import trunc

num = float(input('Digite um Número Real: '))
print(f'o Número {num} tem a parte inteira: {trunc(num)}')

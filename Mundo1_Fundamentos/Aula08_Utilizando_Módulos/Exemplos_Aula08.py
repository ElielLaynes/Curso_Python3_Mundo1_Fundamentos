# Exemplos Práticos
'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A Raiz de {} é igual {}'. format(num, math.ceil(raiz))) # Aqui o módulo ceil de math.ceil() tem a função de arredondar a raiz pra cima.(De forma parecedida com o - :.2f - que formata quantas casas decimais quer que aparece do número).
'''
# IMPORTAÇÀO OTIMIZADA
'''
from math import sqrt, floor # Depois de import se apartar control + espaço ele abre todas módulos/funcionalidades para escolher.
num = int(input('Digite um Número: '))
raiz = sqrt(num) # Com a importação otimizada usa o módulo direto, sem precisar do math antes.
print('A raiz de {} é igual {}'.format(num, floor(raiz))) # Aqui o floor arrendo para baixo.
'''
# Para ver a documentação das bibliotecas padrão do python, acessa esse link >https://docs.python.org/pt-br/3.9/library/index.html<


# EXEMPLO USANDO A BIBLIOTECA RANDOM (para gerar números aleatórios)
import random
num = random.random()
print(num) # Números entre 0 e 1

# Randomizar um número inteiro
import ramdom
num = ramdom.randint(1, 10)
print(num)

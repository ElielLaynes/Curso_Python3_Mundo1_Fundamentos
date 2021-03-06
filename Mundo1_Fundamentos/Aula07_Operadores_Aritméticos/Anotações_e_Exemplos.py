'''
> OPERADORES ARITMÉTICOS

( + ) = Adiçào                      ( ** ) = Potência
( - ) = Subtração                   ( // ) = Divisão Inteira
( * ) = Multiplcação                ( % ) = resto da DivisãO
( / ) = Divisão

>> EXEMPLOS:

5 + 2 == 7                       5 ** 2 == 25
5 - 2 == 3                       5 // 2 == 2
5 * 2 == 10                      5 % 2 ==  1
5 / 2 == 2.5

>> Observação:
Em python, o símbolo de igualdade é representado por 2 sinais de igual(==), enquando apenas 1 sinal de igual(=), quer dizer que estou atribuindo um valor a uma variável.


> ORDEM DE PRECEDÊNCIA DOS OPERADORES
1. () - Parênteses 
2. ** - Potência
3. * , / , // , % - 1: Multiplicação, 2: Divisão, 3: Divisão Inteira, 4: Resti da Divisão 
4. + , - , 1: Soma, 2: Subtração


** Para calcular a potência pode-se usar a função interna pow(), porém, perda a ordem de prededência, mas pode ser usada.
        pow(4, 3) == 64

** Rais quadra de 81
    ***Calcular a raiz quadrade de um número, é a mesma coisa que criar a potência dele por meio(1/2) e raiz cúbica(1/3)
        81 ** (1/2) == 9 # Raiz quadrada
        127 ** (1/3) == 5.0265 # Raiz Cúbica
'''

# PRÁTICA E EXEMPLOS

# Imprimir na tela com fomatação de espaço e ajuste a direita, esqueda ou centralizado

# Com espaço delimitado
nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome)) # Com 20 espaços
print('Praze em te conhecer {:>20}!'.format(nome)) # Justificado a direita
print('Praze em te conhecer {:<20}!'.format(nome)) # Justificado a esquerda
print('Praze em te conhecer {:^20}!'.format(nome)) # Centralizado
print('Praze em te conhecer {:=^20}!'.format(nome)) # Centralizado com sinal igual dos lados

# Formatação de Casas Decimais
        # dentro das chaves coloca {:.2f}, ou seja, .2f(duas casas decimais flutuantes)

n1 = int(input('Digite um valor: '))  
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \nO produto é {} e \nDivisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

# OBSERVAÇÕES:
# Para quebrar uma linha usa \n
# Para não quebrar a linha, imprimir tudo na mesma linha, usa: end=''
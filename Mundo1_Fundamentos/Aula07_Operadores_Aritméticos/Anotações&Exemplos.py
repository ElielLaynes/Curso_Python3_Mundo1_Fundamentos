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
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}'.format(nome))
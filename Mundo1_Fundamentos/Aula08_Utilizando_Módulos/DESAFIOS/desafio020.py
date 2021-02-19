# O mesmo professor do desafio anterior que sorterar a ordem de apresentação dos alunos. Faça um programa que leia os nome dos quatro alinos e mostra a ordem sorteada.


# importando a biblioteca random e usando a função sample para sortear
from random import sample

# Desafio 019
alunos = ['Ana', 'Bernado', 'Caio', 'Débora']
escolha = sample(alunos, 4)
print(escolha)
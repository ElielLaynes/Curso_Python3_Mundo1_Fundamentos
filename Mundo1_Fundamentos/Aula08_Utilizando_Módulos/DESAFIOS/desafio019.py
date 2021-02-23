# Um professor quer sortear um dos seus 4 alunos para apagar o quado, Faça um programa que ajude ele, lendo o nome deles e escreveno o nome do escolhido

# Importando a biblioteca random e usando o método sample
from random import choice

# Desafio 019


alunos = ['Ana', 'Bernado', 'Caio', 'Débora']
escolha = choice(alunos)
print(escolha)
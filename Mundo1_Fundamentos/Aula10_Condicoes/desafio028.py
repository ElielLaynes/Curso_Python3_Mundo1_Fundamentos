# Escreva um programa que faça o computador "pensar" em um número entre 0 e 5
# Peça para o usuário tentar acertar o número escolhido pelo computador
# O Programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

print()
print('============ Jogo da Adivinhação \o/ ============')



computador = randint(0, 5)

usuario = int(input('Qual número o computador está pensando? (número entre 0 e 5)   '))
if usuario == computador:
    print('Parabéns, Você VENCEU! :D ')
else:
    print('Game Over! Você Perdeu! =/ ')

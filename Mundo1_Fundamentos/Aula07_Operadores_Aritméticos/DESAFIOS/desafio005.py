# Faça um programa que leia um número inteiro e moste na tela o seu sucessor e o seu antecessor.

num = int(input('Digite um Número: '))
print(' Você Digitou o número: {0}\n O Sucessor de {1} é: {2}\n E o Antecessor de {3} é: {4}.'.format(num, num, num + 1, num, num - 1))
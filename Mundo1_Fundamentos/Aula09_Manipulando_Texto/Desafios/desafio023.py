# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

    # Exemplo: 

            # Digite um número: 1834

            # unidade: 4
            # dezena: 3
            # centena: 8
            # milhar: 1

print('---------------------------------')

num = str(input('\nDigite um Número entre 0 e 9999: '))

print(f'Você Digitou o número: {num}')

divide = num.split()

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')
# faça um programa que leia uma ANO. Exemplo: (2021).

    # Mostre na tela se o ano é BISSEXTO.

print()
print('===== Esse ano é BISSEXTO? =====')
print()

ano = int(input('Digite um Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} não é BISSEXTO!')
# Faça um programa que leia uma frase pelo teclado e mostre:

    # Quantas vezes aparece a letra "A"
    # Em que posição ela aparece a primeira vez.
    # Em que posição ela aparece a última vez.


frase = str(input('Digite uma Frase: ')).strip()

freq_A = frase.upper().count('A')
pos1_A = frase.upper().find('A')
pos2_A = frase.upper().rfind('A')

print(f'Existem {freq_A} As na frase.')
print(f'A letra A, apareceu a PRIMEIRA vez na Posição: {pos1_A + 1}')
print(f'A letra A, apareceu a ÚLTIMA vez na posição: {pos2_A + 1}')


# Desenvolva um programa que leia o comprimento de Retas

    # Diga ao usuário se as retas PODEM formar um triângulo.

    # Diga ao usuário se as retas NÃO PODEM formar um triângulo.


print()
print(' ===== Essas Retas Podem Forma um Triângulo? =====')
print()

reta1 = float ( input('Primeira Reta: '))
reta2 = float ( input('Segunda Reta: '))
reta3 = float ( input('Terceita Reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print(f'As retas {reta1}, {reta2}, {reta3}, PODEM formar um triângulo.')
else:
    print(f'As retas {reta1}, {reta2}, {reta3}, NÃO PODEM formar um triângulo.')
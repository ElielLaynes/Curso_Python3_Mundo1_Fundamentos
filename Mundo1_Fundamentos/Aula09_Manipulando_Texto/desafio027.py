# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

    #Exemplo:
        # Primeiro = Ana
        # Último = Souza

print()
print('*=' * 50)
print()


nome = str(input('Digite seu Nome: ')).strip()

nome_fatiado = nome.split()

primeiro = nome_fatiado[0]
ultimo = nome_fatiado[ len(nome_fatiado) - 1 ]

print(f'\nOlá {primeiro}, Seja Bem vindo! :D\n')
print(f'Seu Primeiro nome é: {primeiro}\n')
print(f'Seu Último nome é: {ultimo}\n')
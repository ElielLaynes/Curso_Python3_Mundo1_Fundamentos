
# Desenvolva um programa que pergunte a distância de uma viagem em quilômetros(KM)

# Calcule o preço da passagem

        # Viagens ATÉ 200 KM, R$ 0,50 centavos de real por cada 1 KM rodado

        # Viagens ACIMA de 200 KM, R$ 0,45 centavos de real por cada 1 KM rodado

print()

dist_viagem = int(input('Qual a distância da viagem? em (KM):  \n'))

if dist_viagem <= 200:
    preco1 = dist_viagem * 0.50
    print(f'O valor da passagem é igual: R${preco1:.2f}\n')
else:
    if dist_viagem > 200:
        preco2 = dist_viagem * 0.45
        print(f'O valor da passagem é igual: R${preco2:.2f}\n')

print('Obrigado por acessar nosso comparador de passagem =)\n')

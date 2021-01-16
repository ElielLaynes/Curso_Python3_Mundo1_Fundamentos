# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos Dólares ela pode compara
# Cosiderando que, U$$ 1.00 = R$ 3,27

reais = float(input('Quantos Reais você tem? '))
dolar = reais / 3.27
print('Você tem R${:.2f} real(is) e U$${:.2f} Dolar(es)'.format(reais, dolar))
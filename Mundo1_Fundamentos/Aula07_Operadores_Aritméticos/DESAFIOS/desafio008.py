# escreva um programa que leia um valor em metros e exiba convertido em CENTÍMETROS E MILÍMERTROS

metro = float(input('Digite um valor em metros: '))
cent = metro * 1000
mili = metro * 10000
print('{} metros é igual a:\n{:.0f} Centímetros e {:.0f} Milímetros'.format(metro, cent, mili))
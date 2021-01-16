# Faça um programa que leia a largura e a altura de uma parede em METROS, calcule sua ÁREA e a quantidade de tinta necessária para pintá-la. Sabendo que CADA LITRO de tinta, pinta uma ÁREA de 2mˆ2

print('-' * 40)
print('Programa para Calcular quantidade de Tinta')
print('-' * 40)
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print('A área total da parede é de {:.2f} Metros.'.format(area))
print('É necessário {:.2f} Litros de Tinta para Pintá-la.'.format(tinta))
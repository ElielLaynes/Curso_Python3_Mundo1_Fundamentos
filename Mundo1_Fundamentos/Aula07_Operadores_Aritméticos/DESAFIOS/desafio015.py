# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

dias = int(input('Por quantos DIAS o carro foi alugado? '))
km = float(input('Quantos KMs foram percorridos? '))
preco_pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f} reais'.format(preco_pagar))
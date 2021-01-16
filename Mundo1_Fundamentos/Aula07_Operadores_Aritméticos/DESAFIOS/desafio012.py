# Faça um algotitmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Qual o preço do produto? '))
desconto = preco_produto * 0.05
preco_desconto = preco_produto - desconto
print('O preço Atual do Produto é R${:.2f}'.format(preco_produto))
print('APLICANDO 5% de DESCONTO, o NOVO PREÇO desse Produto é R${:.2f}'.format(preco_desconto))

# Faça um programa que leia 3 números

    # Mostre qual é o MAIOR
    # Mostre qual é o MENOR


# inputs de valores
num1 = int ( input( 'Digite um número: ' ) )
num2 = int ( input( 'Digite outro número: ' ) ) 
num3 = int ( input( 'Digite mais um número: ' ))

# Lista armazenando os valores
lista_num = [ num1, num2, num3 ]

# saída retonadando os valores e o maior e menor valor da lista
print ( f'Os número digitados foram: {lista_num}' )
print ()
print ( f'O Maior valor digitado foi: {max(lista_num)}' )
print ( f'O Menor valor digitado foi: {min(lista_num)}' )
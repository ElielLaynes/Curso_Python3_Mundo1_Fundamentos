# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km, mostre um mensagem dizendo que ele foi multado.

# a multa vai custar R$ 7,00 por cada km acima do limite.


velocidade_veiculo = float(input('A qual velocidade(KM) o carro estava? '))

if velocidade_veiculo > 80:

    print('Você foi MULTADO!')   
    multa = (velocidade_veiculo - 80) * 7
    print(f'O valor a ser pago é igual a: R$ {multa:.2f}')

print('Dirija com Segurança!')
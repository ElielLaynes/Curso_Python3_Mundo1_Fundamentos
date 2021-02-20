
# Condição simples

nome = str(input('Qual é o seu nome? '))
if nome == 'Eliel':
    print(f'Nome Bonito, {nome}!')


# Condição composta

nome = str(input('Qual é o seu nome? '))
if nome == 'Eliel':
    print(f'Nome Bonito, {nome}!')
else:
    print('Bom dia :D')



n1 = float(input('Digite a primiera nota: '))
n2 = float(input('Digite a segunda nota:  '))

media = (n1 + n2) / 2
print(f'Sua média foi: {media}')

if media >= 7.0:
    print('Você foi APROVADO! Parabéns :D')
else:
    print('Infelizamente, você foi REPROVADO! :/')


# Usando IF semplificado


n1 = float(input('Digite a primiera nota: '))
n2 = float(input('Digite a segunda nota:  '))

media = (n1 + n2) / 2
print(f'Sua média foi: {media}')

print('Aprovado!' if media >= 7 else 'Reprovado =/')
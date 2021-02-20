
# Cores no terminal em Pyhton

# Utilziando o padrão ANSI - escape sequence

# O código para acionar esse padrão de cores é: \033[m

# Entre o sinal de colchetes e o EME vai o código da cor, exemplo: \033[ aqui vai o código da cor m

# Recebe nenhum ou até 3 códigos que são eles: style - text - background

    # Exemplo:
    #                \033[ stye : text : back m


#                   >>> CÓDIGOS DE COR <<<

''' 
STYLE                                      

0 - sem estilo             
1 - negrito
4 - sublinhado
7 - investe o fundo
com letra


TEXT

30 - BRANCO
31 - VERMELHO
32 - VERDE
33 - AMARELO
34 - AZUL
35 - MAGENTA
36 - CIANO
37 - CINZA

BACKGROUND

40 - BRANCO
41 - VERMELHO
42 - VERDE
43 - AMARELO
44 - AZUL
45 - MAGENTA
46 - CIANO
47 - CINZA

'''

#                        >>> EXEMPLOS <<<

# ordem = style | text | background

# 1 - sem estilo | texto branco | fundo vermelho
print('\033[0;29;41m TESTE 1 \033[m')
# 2 - estilo negrito | texto amarelo | fundo ciano
print('\033[1;33;46m TESTE 2 \033[m')
# 3 - estilo sublinhado | texto magenta | fundo amarelo
print('\033[4;35;43m TESTE 3 \033[m')
# 4 - sem estilo | texto branco | fundo verde
print('\033[0;29;42m TESTE 4 \033[m')
# 5 - invete cores | texto branco | fundo preto
print('\033[7;0;40m TESTE 5 \033[m')
# 6 - invete cores | texto preto | fundo branco
print('\033[7;29m TESTE 6 \033[m')
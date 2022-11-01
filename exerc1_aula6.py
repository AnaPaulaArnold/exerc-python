palavras= ('ana','abacaxi','suco','escola','trabalho')

for palavra in palavras:
    print( '\n Palavra: {}. vogais: '.format(palavra.upper()),end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

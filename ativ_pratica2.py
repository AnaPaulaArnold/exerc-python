def converte (nome): # função para converter o nome
    
    for letra in nome:
        if letra.upper() =='A': # se for letra A substitui para @
            convert.append('@')

        elif letra.upper() =='E': # se for letra E substitui para &
            convert.append('&')

        elif letra.upper() =='I': # se for I substitui para !
            convert.append('!')

        elif letra.upper() =='O': # se for O substitui para #
            convert.append('#')

        elif letra.upper() =='U': #se for U substitui para *
            convert.append('*')
        else:
            convert.append(letra) # se não for nenhum dos casos acima, apenas insere a letra sem converter
    
    #programa principal

nome=input('Digite um nome: ') # recebe o nome para ser convertido
convert=[]
converte(nome.upper()) # chama a função para converter o nome
print(nome.upper()) # imprime nome com letras maiúsculas

for i in convert: # laço para retirar os colchetes da lista na impressão
    for letra in i:
        print(letra, end=' ') # imprime o nome convertido






 




while True:
    nomeCrianca=input('Digite o nome da criança: ') # Recebe o nome para a consulta
    idadeCrianca=int(input('Idade: ')) # Recebe oa idade para a consulta

    if  idadeCrianca<=0: #testa se a idade é válida
        print('Idade inválida, digite novamente')
        continue
   
     
    if 1<=idadeCrianca<=5: # Testa se está na Educação Infantil
        print('A aluna {} tem  {} anos está na Educação Infantil!'.format(nomeCrianca, idadeCrianca))
    elif 6<=idadeCrianca<=10: # Testa se está n Ensino Fundamental I
        print('A aluna {} tem {} anos está no Ensino Fundamental I !'.format(nomeCrianca, idadeCrianca))
    elif 11<=idadeCrianca<=14:# Testa se está no Ensino Fundamental II
        print('A aluna {} tem {} anos está no Ensino Fundamental II !'.format(nomeCrianca, idadeCrianca))
    elif idadeCrianca>=15: # Testa se está no Ensino Medio
        print('A aluna {} tem {} anos está na Ensino Médio!'.format(nomeCrianca, idadeCrianca))

    continuar=int(input('Digite 1 para consultar novamente ou qualquer outra tecla para sair: ')) #Pergunta se deseja continuar ou encerrar a consulta

    if continuar==1: # Se digitar 1 voltará pro ínicio do while
        continue
    else: # Se não irá encerrar...
        print('Encerrando...')
        break
    



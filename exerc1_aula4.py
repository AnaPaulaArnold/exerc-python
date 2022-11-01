for tab1 in range(10):
    for cont in range(10):
     cont+=1
     valor=tab1*cont
     print('Tabuada do {}x{}={}'.format(tab1,cont,valor))
    print('---------------------------------')
    tab1+=tab1 
    valor=0

cadastro={'nome':[], 'sexo':[] , 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? S-sim N-nao: ')
    if terminar.upper() in 'N' or terminar.upper()!='S':
        print('encerrando...')
        break

    nome=input("Qual seu nome? ")
    sexo=input("Qual seu sexo? ")
    ano=int(input("Qual seu ano de nascimento? "))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)

import random
def visualizarInscricao(): # função criada para imprimir os dados da inscrição realizada 
    print('----- Inscrição -----')
    print(' Voucher: {}'.format(novaInscricao['voucher']))
    print(' Nome: {}'.format(novaInscricao['nome']))
    print(' Email: {}'.format(novaInscricao['email']))
    print(' Telefone: {}'.format(novaInscricao['telefone']))
    print(' Curso: {}'.format(novaInscricao['curso']))




def inscricao(): # função criada para a inserção dos dados pelo usuário
    novaInscricao['voucher']=random.randint(1,1000) # utilizado para gerar o número do voucher 
    novaInscricao['nome']=input('Digite seu nome: ')
    novaInscricao['email']=input('Digite seu email: ')
    novaInscricao['telefone']=input('Digite seu telefone: ')
    novaInscricao['curso']=input('Digite o curso: ')
    print('Inscrição realizada com sucesso! Seu voucher é {}'.format(novaInscricao['voucher'])) # retorna sucesso e o num do voucher 


#Programa Principal
print('------ MENU ------') # Imprime as orientações para o usuário
print('1 - Nova Inscrição')
print('2 - Visualizar Inscrição')
print('0 - Encerrar')

inscricoes=[]
novaInscricao={}

while True:
    opcao=int(input('Selecione a opção desejada: ')) # recebe a entrada da opção desejada pelo usuário
    if opcao==1: # chama a função que cria a inscrição
        inscricao()
        inscricoes=novaInscricao
        continue
    elif opcao==2: # chama a função que visualiza a inscrição
        visualizarInscricao()
        continue
    elif opcao==0: # opção que encerra o programa
        print('Encerrando programa ...')
        break
    else: # executa caso o usuário digite uma opção inválida
        print('Digite uma das opções válidas!')
        continue
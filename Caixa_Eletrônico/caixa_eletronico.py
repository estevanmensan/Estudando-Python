# Neste programa devo criar um sistema de caixa eletronico
# Deve conter um menu com as opções: 1- ver saldo; 2- Depositar; 3- Sacar; 4- Extrato; 5- Sair
# Regras: Saldo começa em R$1000; Não permitir saque maior que o saldo;  
#         Guardar todas as operações em uma lista; Mostrar o extrato no final
# Regra extra: impedir depósitos negativos

#Variável saldo
saldo = 1000
#Função que imprime o menu de opções para o usuário
def menu():
    print("| Bem vindo ao Banco Mensan Ltda       |")
    print("| O que desejas?                       |")
    print(" --------------------------------------")
    print("| 1- Ver Saldo                         |")
    print("| 2- Depositar                         |")
    print("| 3- Sacar                             |")
    print("| 4- Extrato                           |")
    print("| 5- Sair                              |")
    print(" --------------------------------------")

#Função para o usuário manter-se operando o sistema
def retorna_ou_sai():
    print(" --------------------------------------")
    print("| Deseja realizar outra operação?")
    print("| 1- Sim \n| 2- Não")
    print(" --------------------------------------")
    while True:
        try:
            retorna = int(input("-> "))
        except ValueError:
            print("Somente 1 ou 2")
        
        if retorna == 1:
            caixa()
        elif retorna == 2:
            break


#Função para a opção 1 - Ver Saldo
def ver_Saldo():
    
    
    print(" --------------------------------------")
    print("|Opção escolhida: Ver Saldo")
    print("|Seu saldo atual é de: ")
    print(f"R${saldo}")
    print(" --------------------------------------")



#Função para a opção 2 - Depositar
def incrementa_Saldo(i):
    saldo_atualizado = saldo + i
    return saldo_atualizado

def depositar():
    print(" --------------------------------------")
    print("|Opção escolhida: Depositar")
    print("|Quanto você deseja depositar? ")
    try:
        qtd = float(input("R$ "))
        print("Dinheiro depositado com sucesso")
        print(f"Quantidade depositada {qtd}")
        incrementa_Saldo(qtd)
        print(incrementa_Saldo(qtd))
    except ValueError:
        print("Por favor, insira somente números!")
    print(" --------------------------------------")
    
    
#Função para funcionalidades
def funcionalidades():
    while True:
        #controle de entrada de dados
        try:
            opcao = int(input("->  ")) #opção do menu (entre 1 e 5)
        except ValueError: 
            print("Você deve inserir um número inteiro")
        
        #condicionais para as opções do menu
        if opcao == 1:
            ver_Saldo()
            retorna_ou_sai()
            break
        elif opcao == 2:
            depositar()
            retorna_ou_sai()
            break
        elif opcao == 3:
            print(f"Opção escolhida: {opcao}")
            break
        elif opcao == 4:
            print(f"Opção escolhida: {opcao}")
            break
        elif opcao == 5:
            print(f"Opção escolhida: {opcao}")
            break
        else:
            print("Por favor, insira um dos valores apresentados no menu!")

def caixa():
    menu() 
    funcionalidades()

caixa()
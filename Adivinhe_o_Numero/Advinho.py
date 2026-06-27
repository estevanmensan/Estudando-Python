import random 

#Função para imprimir o menu do jogo
def menu():
    #Menu da dificuldade
    print("| Advinhe o número que estou pensando |")
    print("| Selecione a dificuldade:            |")
    print("| 1 -> Fácil (Tentativas Ilimitadas)  |")
    print("| 2 -> Médio (10 Tentativas)          |")
    print("| 3 -> Difícil (5 Tentativas)         |")
    print("| 4 -> Sair                           |")


#Função das dificuldades 'Médio' e Difícil
def jogo(chances):
    
    aleatoria = random.randint(1, 100)
    #print(aleatoria)
    
    tentativas = 1
    #0
    # 1
    # 2
    # 3
    # 4
    # 5
#resultado de tentativas é 6
#preciso que ele imprima 5
    while tentativas <= chances: #loop
        try:
            palpite = int(input("Qual o seu palpite?\n"))    #variavel que irá armazenar o palpite do usuário
            if palpite == aleatoria: #se 'palpite' é igual a 'aleatoria' imprime-se a msg e encerra o loop
                print("Parabéns, VOCE ACERTOUUU!!!")
                print(f"Quantidade de tentativas necessárias {tentativas}")
                break
            elif palpite > aleatoria:
                print("Muito alto")
            elif palpite < aleatoria:
                print("Muito baixo")
            tentativas += 1
        except ValueError:
            print("Insira uma variável do tipo inteiro")

    print(f"O valor que pensei era: {aleatoria}")
    print(f"Tentativas {tentativas}")

#Função da dificuldade Fácil
def jogoFacil():
    
    
    aleatoria = random.randint(1, 100)
    #print(aleatoria)
    
    tentativas = 0
    while True: #loop
        try:
            palpite = int(input("Qual o seu palpite?\n"))    #variavel que irá armazenar o palpite do usuário
            if palpite == aleatoria: #se 'palpite' é igual a 'aleatoria' imprime-se a msg e encerra o loop
                print("Parabéns, VOCE ACERTOUUU!!!")
                print(f"Quantidade de tentativas necessárias {tentativas}")
                break
            elif palpite > aleatoria:
                print("Muito alto")
            elif palpite < aleatoria:
                print("Muito baixo")
            else: #Enquanto o usuário errar, será executado o bloco 'else'
                print("Você errou, tente novamente")
            tentativas += 1
        except ValueError:
            print("Insira uma variável do tipo inteiro")


#Função que define a dificuldade e joga
def select_N_play():
    #variável para armazenar a opção
    while True:
        try:
            nivel = int(input("\n- "))
            #condicional para o nível
        except ValueError:
            print("Insira uma variável do tipo inteiro")
        
        if nivel == 1:
            jogoFacil()
            break
            #dificuldade = 'Fácil'
        elif nivel == 2:
            jogo(10)
            break
            #dificuldade = 'Médio'
        elif nivel == 3:
            jogo(5)
            break
            #dificuldade = 'Difícil'
            #print(chances, dificuldade, nivel)
        elif nivel == 4:
            print("Obrigado por jogar!")
            break
        else:
            print("Coloque um dos valores do menu!!!")
        

#Execução das funções
menu()
select_N_play()



import random
print("======= Bem vindo ao jogo de adivinhação! =======")
    
    

#var
numerosecreto = random.randrange(1,101) 
total_de_tentativas = 0
rodada = 1
pontos = 1000


print ("Escolha nível de jogo:")
print ("(1) - fácil, (2) médio e (3) difícil")
nivel = int(input ("Digite: ")) #define o nível que vai ser jogado na var nivel
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):   
    total_de_tentativas = 10
else:   
    total_de_tentativas = 5




for rodada in range (1, total_de_tentativas + 1):   #limite do número de tentativas
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))     
    chute = int(input("Digite um número de 1 a 100: "))   
    print("Você digitou: ", chute)
        #converte uma str para o int (números inteiros)
    
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número de 1 a 100")
        continue
    


    acertou = numerosecreto == chute
    maior = chute > numerosecreto
    menor = chute < numerosecreto

    if (acertou):
        print("Você acertou, você fez: {} pontos!".format(pontos))
        break
    
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        
        
        pontos_perdidos = abs(numerosecreto - chute)
        pontos = pontos - pontos_perdidos
        print ("pontos: ", pontos)


    rodada = rodada + 1     # o número de rodadas aumenta a cada loop


print("Fim do jogo, o número era: ", numerosecreto)

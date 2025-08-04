import random
print("############################")
print("#    jogo de adivihação    #")
print("#          gustavo         #")
print("############################")
print("seja bem vindo ao game 👾💤 ")

numeroSecreto= random.radrange(0,100)
totaltentativas = 0
pontos = 100

print("qual niveis de dificultade?")
print("(1) - fácil (2) - médio (3) - Dificil ")

nivel = int(input("Escolha um nivel"))

if(nivel == 1):
    print("20 tentativas")
    totaltentativas = 20
elif(nivel == 2):
    print("10 tentativas")
    totaltentativas = 10
elif(nivel ==2) :
    print("5 tentativas")
    totaltentativas = 5


for rodada in range (1,totaltentativas + 1) :
    print("Tentativa {} de {}" .format(rodada,totaltentativas) )
    chute_str = input("digite um numero entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or > 100:)
       print("numero invalido")
       continue
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto
    
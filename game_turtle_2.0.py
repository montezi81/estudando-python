from time import sleep
from turtle import Turtle
# Inicando a turtle
t = Turtle()
# Definir velocidade
t.speed(1)

inicio = input('Deseja começar o jogo S(sim) ou N(não) ?')
if inicio == 'S':
    while True:
        frente_tras = input('Deseja ir para frente(F) ou para trás(T).')
        distancia = float(input('Qual a distância percorrida em px ? '))
        rotacao = input('Deseja rotacionar para esquerda(E), direita(D) ou não rotacionar(N)? ')
        distancia_rotacao = float(input('Quantos graus deseja rotacionar ?'))
        continua = input('Deseja continuar (S) ou (N) ?')

        if frente_tras == 'F':
            t.forward(distancia)
        elif rotacao == 'D':
            t.right(distancia_rotacao)
        elif rotacao == 'E':
            t.left(distancia_rotacao)
        elif frente_tras == 'T':
            t.backward(distancia)
        elif rotacao == 'D':
            t.right(distancia_rotacao)
        elif rotacao == 'E':
            t.left(distancia_rotacao)
        elif continua == 'S':
            continue
        elif continua == 'N':
            print ('Saindo do sistema em 3,2,1...')
            sleep(3)
            break    


        
            

else:
    print('Saindo...')
    sleep(3)


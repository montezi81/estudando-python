from turtle import Turtle
# Inicando a turtle
t = Turtle()
# Definir velocidade
t.speed(1)
jogo = input(print('Olá desje começar o jogo S ou N ?'))
if jogo == 'S':
    while True:
        frente_tras = input(print('Deseja ir para frente(F) ou para trás(T)?')).upper
        if frente_tras == 'F':
            t.forward(90)
        else:
            t.backward(90)

        angulo = input(print('Qual angulo deseja mover esquerda(E) ou direita(D)?')).upper
        if angulo == 'E':
            t.left(90)
        else:
            t.right(90)
        
else:
    print('Até logo')
    




'''
distancia = int(input('Distância a percorrer ?'))
t.forward(distancia)
# Movimentar para frente
t.forward(100)
# Rotacionar para direita em x graus
t.right(90)
t.forward(100)
# Rotacionar para esquerda em x graus
t.left(90)
t.forward(100)
# Movimentar a turtle para trás
t.backward(200)
input()
'''
import random

#cara ou coroa
sorte = ['cara', 'coroa']
print('A opção foi:', random.choice(sorte))

#sorteio de nome
nomes = ['Marcos', 'Roberta', 'Maria', 'Vinícius', 'Clarinha']
print('O nome sorteado é:', random.choice(nomes))

#número aleatório entre 10 e 100
numero = random.randint(1,100)
print('O número entre 1 e 100, foi ==>', numero)

#Embaralhando
cartas = ['Paus', 'Copas', 'Espada', 'Ouro']
random.shuffle(cartas)
print('O embaralhamento foi ' ,cartas)

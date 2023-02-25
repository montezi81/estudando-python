# Laço de repetição
# Range gera um valor
for numero in range(1,6):
    print('Carregando...', numero)

#step, vai pulando de 2 e 2
for pulando in range(1,20,2):
    print('Carregando', pulando)

#imprimindo listas
nomes = ['Marcos', 'João', 'Pedro', 'Barnabé']
for nome in nomes:
    print(nome)


# Desafios

for desafio1 in range(18,111):
    print('Estamos em', desafio1)

for desafio2 in range(1,11):
    #print('Realizando Passo', desafio2)
    print(f'Executando Passo {desafio2}')

for x in range (1,100,15):
    print(f'Posição {x}')

for y in range (10,500,30):
    print(f'Executando passo...{y}')

for w in range (-5,750,100):
    print(f'Testando...{w}')


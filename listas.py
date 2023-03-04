# Acessando listas com python

precos = [0,1,3,5,6,8,300,500,1000,1500,2000]
print(precos[3])
# Indice 3
# Será impresso a posição 3, o número 5.
# Quando não sei qual é o indice, coloco a função .index e digo qual o valor que estou procurando entre parenteses.
print(precos[precos.index(1000)])
print(precos[precos.index(8)])

# As listas aceitam qualquer valor
itens = [0,1,2,3,4,5,6,'Mamão', 'Alface', 'Cebola', 5.55, 6.99, 7.55]
print(itens[5])

# Repetição de valores

lista_de_nomes = ['Marcos'] * 10
lista_de_numeros = [9] * 10
print(lista_de_nomes)
print(lista_de_numeros)

# Usando o gerador range com uma sequencia de valores
# Gerando lista de 1 a 29
lista = list(range(30))
print(lista)
# Gerando uma lista de caracteres
lista_de_caracteres = list('Bem-vindo ao python')
print(lista_de_caracteres)

# Criando uma lista dentro de outra lista
lista_matriz = [['Marcos', 41], ['Roberta', 43], ['Maria Clara', 14]]
print(lista_matriz[0])
# Acesando +1 nível dentro da lista
print(lista_matriz[0][0])



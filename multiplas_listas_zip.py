from itertools import zip_longest

lista_a = ['Marcos', 'Roberta', 'Maria']
lista_b = [41,42,14]

for a,b in zip (lista_a, lista_b):
    print(a)
    print(b)

produtos = ['Maçã', 'Uva', 'Pera', 'Caju']
preços = [2.55, 3.99, 4.99, 5.00]

for a,b in zip(produtos, preços):
    print(f'O produto {a} tem o preço de {b} ')

# Multiplas listas aonde a primeira lista possui quantidade maior de itens
# Por isso a importação da biblioteca itertools zip longest
titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'O titulo é {titulo} seguindo a descrição {descricao}')


# Desafio

# temos uma lista não simetrica, cada lista possui um numero diferente de informações.
# Temos que usar biblioteca itertools zip longest
produtos_A = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
preços_A = ['R$ 500,00', 'R$ 1500,00', 'R$ 2700,00', 'R$ 5000,00']
for prod, preco in zip_longest(produtos_A, preços_A):
    print(f'Produto: {prod} encontrado no valor de {preco}')

# Argumentos posicionais
# Devo posicionar na função o nome da variável de forma sequencial
# Exemplo: (nome_produto, preço), quando chamo a função o primeiro a ser chamado deve ser nome_produto e depois o preço.
# Aoós o *, os argumentos devem ser nomeados.

def exibir_preco(nome_produto, *, preço):
    print(f'Nome do produto: {nome_produto}')
    print(f'Preço do produto: {preço}')

# exibir_preco('Iphone', 10.000) ==> O * obriga a nomear os argumentos.
exibir_preco(nome_produto='Iphone', preço='10.000')

# Aonde o posicional não importa ? Qual o cenário ?
# No caso abaixo:
# Argumentos nomeados
exibir_preco(nome_produto='Iphone', preço='10.000')
exibir_preco(preço='10.000', nome_produto='Iphone')


# Desafio

def gerar_objeto_personalizado(cor,*, altura, formato):
    print(f'A cor será {cor}, na parede de {altura}, no formato {formato}')

# O primeiro argunto será posicional e outros 2 obrigatoriamente deverão ser nomeados.
gerar_objeto_personalizado('Vermelho', altura='1.75', formato='Circular' )


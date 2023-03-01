# Funções

# input()
# len()
# split()

# O que elas tem em comum ?

# def nome_da_funcao(parametros)

def dar_boas_vindas():
    print('Bem vinda')

dar_boas_vindas()

def dar_boas_vindas_personal(nome):
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personal('Marcos')

# Valor padrão

def apresentar_lugar(lugar='Nossa loja'):
    print(f'Conheça {lugar}')

apresentar_lugar()

def apresentar_lugar_versao(horario_de_funcionamento, lugar='Nossa loja'):
    print(f'Conheça {lugar}, horário de funcionamento {horario_de_funcionamento}')

apresentar_lugar_versao('08:00 as 18:00')

# Desafio Nome e Sobrenome

def gerar_nome_completo(nome, sobrenome):
    print(f'O nome é {nome} e o sobrenome é {sobrenome}')

gerar_nome_completo('Marcos', 'Costa')


# Desafio preço e quantidade

def calcular_valores(preço, qtd=1):
    print(preço * qtd)

calcular_valores(500, 5)

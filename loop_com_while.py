# Laço com While

tentativas = 0
while tentativas < 3:
    print('Tente novamente')
    tentativas += 1

# Senha
senha = ''
while senha != '123456':
    senha = input('Digite sua senha: ')
print('bem vindo !')

# Preenchimento obrigatório
nome = ''
while nome == '':
    nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')

# Contadores
horario = 0
while horario <= 17:
    print(f'Ainda não começou opor do sol {horario}...')
    horario +=1
print('O por do sol vai começar !')

# Contagem regressiva
contador = 100
while contador >= 0:
    print(contador)
    contador -=1


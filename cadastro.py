# CADASTRE-ME
# Parte 1

import datetime
from datetime import datetime
import random
import time

print('--- Sistem de cadastro de funcionários ---')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
#data_do_cadastro = datetime.date.today()
data_do_cadastro = datetime.now()
data_do_cadastro_str = data_do_cadastro.strftime("%d/%m/%Y %H:%M")
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)
data_de_nascimento = input('Digite a data do seu nascimento: ')

time.sleep(2)
print('...')
print('Por favor aguarde...')
time.sleep(2)
time.sleep(1)
print('...')


# Parte 2
# Boas-Vindas
print(15 * '--------')
print('Olá' ,nome,',Seja bem-vindo! Seu registro foi concluido com sucesso no dia', data_do_cadastro_str, '!')
print('Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de', sorteio, '!')
print(15 * '--------')


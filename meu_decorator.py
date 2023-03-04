from datetime import datetime

def desafio(horario): # Criei a função
    def teste1(): # Criei uma nova função executando a função que foi passada para ele
        print(datetime.now()) # Antes de executar a função imprimo a data atual
        horario() # executo a função que foi passada
        print(datetime.now()) # imprimo o horario atual
    return teste1 # retorno a referencia



@desafio 
# Usando o decorator, na função desafio_1
# O decorator é para reutilizar funções dentro dos códigos
def desafio_1():
    print('Testando...')

desafio_1()
import datetime
from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

lancamento = datetime(2023, 2, 28)
print(lancamento)

#Convertendo o formato de data
data_lancamento = datetime.strptime(input('Qual a data de lançamento ? '), '%d/%m/%Y')
print('Data de lançamento: ', data_lancamento)

data_futura = datetime.now()
prazo = data_lancamento - data_futura
print('o prazo é de', prazo.days, 'dias')



## Meu aniversário

aniversario = datetime(2023, 10, 3)
dias_para_aniversario = aniversario - datetime.now()
print('Faltam quantos dias para o aniversário: ', dias_para_aniversario)

# Para receber vários argumentos nos valores (colocar o *)
# Conhecido com *args
def somar(*valores, b):
    print(valores)
    for valor in valores:
        b+= valor
    print(b)

# Tuplas (lista de valores)
# Diversos valores no mesmo parâmetro
somar(10,20,5,20, b=5)
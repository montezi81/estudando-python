# Loop Aninhados
# País + Estação

#paises = ['Brasil', 'Paraguai', 'Italia', 'Vaticano', 'EUA']
#estacoes_do_ano = ['Primavera', 'Verao', 'Outuno', 'Inverno']

# Um for dentro de outro for
# for país in paises:
#     for estacoes in estacoes_do_ano:
#         print(f'O País {país} está na estação {estacoes}')


# for x in range (1,10):
#     for y in range (2,12):
#         for w in range (3,13):
#             print(f'Externo {x}, interno {y} e {w}')


# Desafio         

celulares = ['Asus', 'Samsung', 'Sony', 'Iphone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for fabricante in celulares:
    for version in versoes:
        print(f'Celular do fabricante {fabricante} é do modelo {version}')

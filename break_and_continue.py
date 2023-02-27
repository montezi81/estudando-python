# Continue
# Ignogar ou pular, um laço

for numero in range (100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue

# Break

for numero in range (100):
    if numero % 2 == 0:
        print(numero)
    else:
        break


frutas = ['Maça', 'Pêra', 'Uva', 'Manga', 'Caqui']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta')


frutas = ['Maça', 'Pêra', 'Uva', 'Manga', 'Caqui']
for fruta in frutas:
    if fruta == 'Manga':
        break
    print(f'{fruta} adicionada a dieta')

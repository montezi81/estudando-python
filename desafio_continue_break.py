estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    else:
        print(f'{estilo} é um estilo musical')


estilos_musicais = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilos_musicais_x in estilos_musicais:
    if estilos_musicais_x == 'Rock':
        break
    else:
        print(f'{estilos_musicais_x}')

teclado = 'Teclado'
print(teclado[3])
print(teclado[2])

frase = 'Texto muito grande para localizar a String'
print(frase[-1])
print(frase.index('t'))
print(frase[frase.index('t')])
print(frase[0:6])
print(frase[0:])
print(frase[6:])
print(frase[:-7])
print(frase.rindex('t'))

biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

desenvolvimento = 'Desenvolvimento De Aplicações'
indice_d = desenvolvimento.rindex('D')
indice_s = desenvolvimento.rindex('s')
print(desenvolvimento[indice_d:indice_s+1])


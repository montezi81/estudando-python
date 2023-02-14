frase = 'Este é um teste de matemática, prepare-se !'
print(frase.split())
# Separa na string o que estiver na vírgula
print(frase.split(','))
# Separa na string o que estiver no hífen
print(frase.split('-'))

nomes = 'João, Pedro, Thiago, Tomé, Marcos, Bartolomeu, Tadeu'
print(nomes.split())
print(nomes.split(','))

hashtags = ' #code, #python, #developer, #course, #test'
print(hashtags.split('#'))
print(hashtags.split('#', 3))

hashtags_separadas = hashtags.split(' ')
print(hashtags_separadas)
print('-'.join(hashtags_separadas))
print(' *** '.join(hashtags_separadas))
print(' @ '.join(hashtags_separadas))
print('    '.join(hashtags_separadas))

print('##########FIM DO TREINAMENTO##########')

### DESAFIO ###
frase1 = 'Desafio manipulação de strings'
palavras1 = frase1.split()
print(','.join(palavras1))

frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split(',')
print(' & '.join(palavras2))



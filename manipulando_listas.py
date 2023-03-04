valores = [10,20,30,40,50,60,70,2,22,222,2222]
anos = [2020,2021,2022,2023,2024,2025,2026,2027,2028]

# Adicionar número na lista valores
valores.append(11)
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

# Adicionar listas
nova_lista = valores + anos
print(nova_lista)

# Indice
print(anos[1])

# onde inserir e qual o valor 
# Inserir valor dentro da lista
anos.insert(2,2031)
print(anos)

# Extrair com base no indice
anos_2020 = anos.pop(0)
print(anos_2020)

#Excluindo
anos.remove(2023)
print(anos)
#Excluindo da lista
del anos[2]
# excluindo do indice x até y
del anos[2:6]

# Contando na lista
print(valores.count(2))
# Quantas vezes apareceu na lista o número 2

# Resetar os itens dentro da lista
valores.clear()
print(valores)






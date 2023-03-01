
# Esta função apenas processa um dado.
def exibir_moeda(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_moeda('usd')


# No caso do return, vou precisar da função que estão dentro dela para seguir com o fluxo do programa.

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
    
cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em ações')
else:
    print('Cotação na favorável')
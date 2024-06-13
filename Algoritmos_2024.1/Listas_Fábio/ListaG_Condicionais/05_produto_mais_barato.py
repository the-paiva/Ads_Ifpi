#Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
#sempre pelo mais barato.

from Utils.io_utils import pedir_float_min, pedir_string

#Escreve a tabela dos produtos e seus respectivos preços
def escrever_tabela(produto1, produto2, produto3, preco1, preco2, preco3):
    print('\n-------------- TABELA DE PREÇOS --------------')
    print(f'{produto1}: R$ {preco1:.2f}')
    print(f'{produto2}: R$ {preco2:.2f}')
    print(f'{produto3}: R$ {preco3:.2f}')
    print('----------------------------------------------')

#Informa qual produto deve ser comprado caso haja apenas um produtos mais barato
def informar_melhor_produto_unico(preco1, preco2, preco3, produto1, produto2, produto3):
    if preco1 < preco2 and preco1 < preco3:
        melhor_produto = produto1
    elif preco2 < preco1 and preco2 < preco3:
        melhor_produto = produto2
    else:
        melhor_produto = produto3

    print(f'\nProduto que deve ser comprado: {melhor_produto}')

#Informa quais produtos devem ser comprados caso hajam dois produtos mais baratos
def informar_dois_melhores_produtos(preco1, preco2, preco3, produto1, produto2, produto3):
    if preco1 == preco2:
        melhor_produto1 = produto1
        melhor_produto2 = produto2
    elif preco1 == preco3:
        melhor_produto1 = produto1
        melhor_produto2 = produto3
    else:
        melhor_produto1 = produto2
        melhor_produto2 = produto3

    print('\nHá duas opções opções possíveis de produto')
    print(f'1º: {melhor_produto1}')
    print(f'2º: {melhor_produto2}')

def main():
    produto1 = pedir_string('\nDigite o nome do primeiro produto: ')
    preco1 = pedir_float_min('Digite o preço: ', min=0.1)
    produto2 = pedir_string('\nDigite o nome do segundo produto: ')
    preco2 = pedir_float_min('Digite o preço do segundo produto: ', min=0.1)
    produto3 = pedir_string('\nDigite o nome do terceiro produto: ')
    preco3 = pedir_float_min('Digite o preço do terceiro produto: ', min=0.1)

    escrever_tabela(produto1, produto2, produto3, preco1, preco2, preco3)

    if preco1 == preco2 == preco3:
        print('\nTodos os produtos têm preços iguais!')
    else:
        if ((preco1 < preco2 and preco1 < preco3) or (preco2 < preco1 and preco2 < preco3) or
        (preco3 < preco1 and preco3 < preco2)):
            informar_melhor_produto_unico(preco1, preco2, preco3, produto1, produto2, produto3)
        else:
            informar_dois_melhores_produtos(preco1, preco2, preco3, produto1, produto2, produto3)

main()

#Escreva um algoritmo que leia o nome de um produto, o preço e a quantidade comprada. Escreva o
#nome do produto comprado e o valor total a ser pago, considerando que são oferecidos descontos pelo
#número de unidades compradas, segundo a tabela abaixo: (FLAG: nome do produto = “FIM”).
#a. Até 10 unidades: valor total
#b. de 11 a 20 unidades: 10% de desconto
#c. de 21 a 50 unidades: 20% de desconto
#d. acima de 50 unidades: 25% de desconto

from Utils.io_utils import pedir_string, pedir_float_min, pedir_int_min

#Calcula o valor do desconto que vai ser aplicado de acordo com a quantidade de unidades compradas
def calcular_desconto(quantidade):
    if quantidade <= 10:
        return 0
    elif quantidade <= 20:
        return 0.10
    elif quantidade <= 50:
        return 0.20
    else:
        return 0.25   

#Calcula o valor total da compra
def calcular_valor_total(preco, quantidade, desconto):
    valor_total = preco * quantidade
    valor_com_desconto = valor_total * (1 - desconto)
    
    return valor_com_desconto

def main():
    nome_do_produto = ''

    while nome_do_produto != 'FIM':
        nome_do_produto = pedir_string('Digite o nome do produto (ou "FIM" para encerrar): ').upper()
        
        if nome_do_produto != "FIM":
            preco = pedir_float_min('Digite o preço do produto: R$ ', 0.1)
            quantidade = pedir_int_min('Digite a quantidade comprada: ', 1)

            desconto = calcular_desconto(quantidade)
            valor_total = calcular_valor_total(preco, quantidade, desconto)
            
            print(f'\nProduto: {nome_do_produto}')
            print(f'Valor total a pagar: R$ {valor_total:.2f}\n')

main()

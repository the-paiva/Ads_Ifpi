#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#   Até 5 Kg                Acima de 5 Kg
#Morango: R$ 2,50 por Kg    R$ 2,20 por Kg
#Maçã: R$ 1,80 por Kg       R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
#(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
#pelo cliente.

from Utils.io_utils import pedir_float_min

#Ajusta o preço do quilo do produto de acordo com a quantidade que está sendo comprada
def ajustar_preco_kg(peso_kg, preco_kg_original):
    if peso_kg >= 5:
        return preco_kg_original - 0.3
    
    return preco_kg_original

#Ajusta o valor final a ser pago pelo cliente de acordo com o peso ou o próprio valor total das compras
def ajustar_valor_total(peso_total, valor_total):
    if peso_total > 8 or valor_total > 25:
        return valor_total - (valor_total * 10 / 100)
    
    return valor_total

#Escreve um relatório com o valor individual de cada produto e o valor total a ser pago
def mostrar_relatorio_da_compra(valor_morango, valor_maca, valor_total):
    print('=============================================================')
    print(f'Valor dos morangos: R$ {valor_morango:.2f}')
    print(f'Valor das maçãs: R$ {valor_maca:.2f}')
    print(f'Valor total a ser pago: R$ {valor_total:.2f}')

def main():
    peso_kg_morango = pedir_float_min('\nDigite a quantidade de morangos a serem comprados (Kg): ', 0.3)
    peso_kg_maca = pedir_float_min('Digite a quantidade de maçãs a serem compradas (Kg): ', 0.3)
    
    preco_kg_morango = 2.5
    preco_kg_maca = 1.8
    preco_kg_morango = ajustar_preco_kg(peso_kg_morango, preco_kg_morango)
    preco_kg_maca = ajustar_preco_kg(peso_kg_maca, preco_kg_maca)

    peso_total = peso_kg_morango + peso_kg_maca
    valor_morango = peso_kg_morango * preco_kg_morango
    valor_maca = peso_kg_maca * preco_kg_maca
    valor_total = valor_morango + valor_maca
    valor_total = ajustar_valor_total(peso_total, valor_total)

    mostrar_relatorio_da_compra(valor_morango, valor_maca, valor_total)

main()

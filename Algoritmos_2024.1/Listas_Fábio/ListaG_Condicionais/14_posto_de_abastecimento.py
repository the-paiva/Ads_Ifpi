#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#1. Álcool:
#· até 20 litros, desconto de 3% por litro
#· acima de 20 litros, desconto de 5% por litro
#2. Gasolina:
#· até 20 litros, desconto de 4% por litro
#· acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
#seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se 
#que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

from Utils.io_utils import pedir_int_min, pedir_string
from time import sleep

def escrever_cabecalho():
    print('\n========== POSTO DE ABASTECIMENTO ROGÉRIO ROMÂNTICO ==========')
    print('A - Álcool')
    print('G - Gasolina')
    print('===============================================================')

def eh_combustivel_valido(tipo_combustivel):
    if tipo_combustivel == 'A' or tipo_combustivel == 'G':
        return True

    return False

#Calcula o valor do álcool de acordo com a quantidade de litros digitada pelo usuário
def calcular_valor_alcool(quant_litros):
    if quant_litros <= 20:
        preco_alcool = 1.9 - (1.9 * 3 / 100)
    else:
        preco_alcool = 1.9 - (1.9 * 5 / 100)

    return quant_litros * preco_alcool

def calcular_valor_gasolina(quant_litros):
    if quant_litros <= 20:
        preco_gasolina = 2.5 - (2.5 * 4 / 100)
    else:
        preco_gasolina = 2.5 - (2.5 * 6 / 100)

    return quant_litros * preco_gasolina

def main():
    escrever_cabecalho()

    tipo_combustivel = pedir_string('Digite o tipo de gasolina: ').upper()

    if eh_combustivel_valido(tipo_combustivel):
        quant_litros = pedir_int_min('Digite a quantidade de litros: ', 1)

        if tipo_combustivel == 'A':
            valor_a_pagar = calcular_valor_alcool(quant_litros)
        else:
            valor_a_pagar = calcular_valor_gasolina(quant_litros)

        print(f'Valor a ser pago: R$ {valor_a_pagar:.2f}')
    else:
        print('Tipo de combustível inválido! Encerrando o programa...')
        sleep(3)
    
main()

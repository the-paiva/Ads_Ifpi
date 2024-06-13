#Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
#11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
#ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR:
#* Salário Bruto até R$ 900,00 (inclusive) - isento
#* Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
#* Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
#* Salário Bruto acima de R$ 2.500,00 - desconto de 20%
#Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
#a quantidade de hora é 220.
#* Salário Bruto: (5 * 220) : R$ 1100,00
#* (-) IR (5%) : R$ 55,00
#* (-) INSS ( 10%) : R$ 110,00
#* FGTS (11%) : R$ 121,00
#* Total de descontos : R$ 165,00
#* Salário Liquido : R$ 935,00

from Utils.io_utils import pedir_float_min, pedir_int_min
from Utils.math_utils import calcular_porcentagem

#Escreve o relatório do salário e todos os descontos aplicados
def escrever_relatorio(valor_hora, horas_trabalhadas, salario_bruto, percentual_ir, desconto_ir, 
desconto_inss, valor_fgts, total_descontos, salario_liquido):
    print(f'\nSalário Bruto: {valor_hora:.2f} * {horas_trabalhadas} = R$ {salario_bruto:.2f}')
    print(f'(-) IR ({percentual_ir}%): R$ {desconto_ir:.2f}')
    print(f'(-) INSS (10%): R$ {desconto_inss:.2f}')
    print(f'FGTS (11%): R$ {valor_fgts:.2f}')
    print(f'Total de descontos: R$ {total_descontos:.2f}')
    print(f'Salário Líquido: R$ {salario_liquido:.2f}')

#Retorna o percentual de imposto de renda que será aplicado
def retornar_percentual_de_ir(salario_bruto):
    if salario_bruto <= 900:
        return 0
    elif salario_bruto <= 1500:
        return 5
    elif salario_bruto <= 2500:
        return 10

    return 20

def main():
    valor_hora = pedir_float_min('\nDigite o valor da hora de trabalho: R$ ', 1)
    horas_trabalhadas = pedir_int_min('Digite quantas horas foram trabalhadas no mês: ', 1)

    salario_bruto = valor_hora * horas_trabalhadas
    percentual_ir =  retornar_percentual_de_ir(salario_bruto)
    desconto_ir = calcular_porcentagem(salario_bruto, percentual_ir)
    PERCENTUAL_INSS = 10
    desconto_inss = calcular_porcentagem(salario_bruto, PERCENTUAL_INSS)
    PERCENTUAL_FGTS = 11
    valor_fgts = calcular_porcentagem(salario_bruto, PERCENTUAL_FGTS)
    total_descontos = desconto_inss + desconto_ir
    salario_liquido = salario_bruto - total_descontos

    escrever_relatorio(valor_hora, horas_trabalhadas, salario_bruto, percentual_ir, desconto_ir,
    desconto_inss, valor_fgts, total_descontos, salario_liquido)

main()

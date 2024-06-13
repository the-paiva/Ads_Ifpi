#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
#salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#* salários até R$ 280,00: aumento de 20%
#* salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#* salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#* salários de R$ 1500,00 em diante : aumento de 5% 
#Após o aumento ser realizado, informe na tela:
#* o salário antes do reajuste;
#* o percentual de aumento aplicado;
#* o valor do aumento;
#* o novo salário, após o aumento.

from Utils.io_utils import pedir_float_min
from Utils.math_utils import calcular_porcentagem

#Escreve o resultado do reajuste do salário
def escrever_resultado_do_reajuste(salario_base, salario_reajustado, percentual, reajuste):
    print(f'\nSalário base: R$ {salario_base:.2f}')
    print(f'Percentual de aumento: {percentual} %')
    print(f'Valor do aumento: R$ {reajuste:.2f}')
    print(f'Salário reajustado: R$ {salario_reajustado:.2f}')

#Retorna o percentual de reajuste que deve ser aplicado
def retornar_percentual_de_reajuste(salario_base):
    if salario_base <= 280:
        return 20
    elif salario_base <= 700:
        return 15
    elif salario_base <= 1500:
        return 10
    
    return 5

def main():
    salario_base = pedir_float_min('\nDigite o salário do funcionário: R$ ', 100)

    percentual = retornar_percentual_de_reajuste(salario_base)
    reajuste = calcular_porcentagem(salario_base, 20)
    salario_reajustado = salario_base + reajuste

    escrever_resultado_do_reajuste(salario_base, salario_reajustado, percentual, reajuste)

main()

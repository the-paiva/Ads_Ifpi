#Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
#descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
#somas. (Flag: salário=0)
#
#   De              Até             Acréscimo
#   R$ 0,00         R$ 2.999,99     25 %
#   R$ 3.000,00     R$ 5.999,99     20 %
#   R$ 6.000,00     R$ 9.999,99     15 %
#   Acima de R$ 10.000,00           10 %

from Utils.io_utils import pedir_float_min

#Calcula o reajuste do salário de um funcionário de acordo com a tabela de reajustes
def reajustar_salario(salario_atual):
    if salario_atual <= 2999.99:
        return salario_atual + (salario_atual * 0.25)
    elif salario_atual <= 5999.99:
        return salario_atual + (salario_atual * 0.2)
    elif salario_atual <= 9999.99:
        return salario_atual + (salario_atual * 0.15)
    else:
        return salario_atual + (salario_atual * 0.1)

#Mostra os resultados relacionados aos salários e seus reajustes 
def mostrar_resultados(soma_dos_salarios_atuais, soma_dos_salarios_reajustados, diferenca_das_somas):
    print('\n========================= RELATÓRIO =========================')
    print(f'Soma dos salários atuais: R$ {soma_dos_salarios_atuais:.2f}')
    print(f'Soma dos salários reajustados: R$ {soma_dos_salarios_reajustados:.2f}')
    print(f'Diferença das somas: R$ {diferenca_das_somas:.2f}')
    print('=============================================================')

def main():
    soma_dos_salarios_atuais, soma_dos_salarios_reajustados = 0, 0
    salario_atual = -1

    while salario_atual != 0:
        salario_atual = pedir_float_min('\nDigite o salário atual de algum funcionário: R$ ', 0)

        salario_reajustado = reajustar_salario(salario_atual)
        soma_dos_salarios_atuais += salario_atual
        soma_dos_salarios_reajustados += salario_reajustado

        #Ex: R$ 1000.00 -> R$ 1250.00
        print(f'R$ {salario_atual:.2f} -> R$ {salario_reajustado:.2f}')

    diferenca_das_somas = soma_dos_salarios_reajustados - soma_dos_salarios_atuais

    mostrar_resultados(soma_dos_salarios_atuais, soma_dos_salarios_reajustados, diferenca_das_somas)

main()

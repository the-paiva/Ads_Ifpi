#Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
#nascimento e a data (dia, mês e ano) atual.

from Utils.io_utils import pedir_int_min_max
from Utils.general_utils import eh_data_valida
from Utils.math_utils import eh_maior

def main():
    print('\n================== Analisador de idade ==================')

    dia_nasc = pedir_int_min_max('\nDigite o dia do seu nascimento: ', 1, 31)
    mes_nasc = pedir_int_min_max('Digite o mês do seu nascimento: ', 1, 12)
    ano_nasc = pedir_int_min_max('Digite o ano do seu nascimento: ', 1900, 2024)

    dia_atual = pedir_int_min_max('\nAgora digite o dia atual: ', 1, 31)
    mes_atual = pedir_int_min_max('Digite o mês atual: ', 1, 12)
    ano_atual = pedir_int_min_max('Digite o ano atual: ', 1900, 2024)

    if eh_data_valida(dia_nasc, mes_nasc, ano_nasc) and eh_data_valida(dia_atual, 
    mes_atual, ano_atual) and (eh_maior(ano_atual, ano_nasc) or eh_maior(mes_atual,
    mes_nasc) or eh_maior(dia_atual, dia_nasc)):
        print('\nTodas as datas digitadas são válidas!')
    else:
        print('\nErro! Alguma das datas digitadas é inválida, revise os valores...')
        main()

main()

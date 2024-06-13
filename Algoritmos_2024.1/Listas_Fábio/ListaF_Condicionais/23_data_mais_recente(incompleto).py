#Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual 
#delas é a mais recente. 

#O.B.S: Código INCOMPLETO

from Utils.io_utils import pedir_int_min, pedir_int_min_max
from Utils.general_utils import eh_data_valida

def main():
    ano1 = pedir_int_min('\nDigite o primeiro ano: ', 1)
    mes1 = pedir_int_min_max('Digite o primeiro mês: ', 1, 12)
    dia1 = pedir_int_min_max('Digite o primeiro dia: ', 1, 31)

    ano2 = pedir_int_min('\nAgora digite o segundo ano: ', 1)
    mes2 = pedir_int_min_max('Digite o segundo mês: ', 1, 12)
    dia2 = pedir_int_min_max('Digite o segundo dia: ', 1, 31)

    if eh_data_valida(dia1, mes1, ano1) and eh_data_valida(dia2, mes2, ano2):
        print(f'\nPrimeira data: {dia1}/{mes1}/{ano1}')
        print(f'Segunda data: {dia2}/{mes2}/{ano2}')

        if ano1 > ano2 or mes1 > mes2 or dia1 > dia2:
            print('\nA primeira data é mais recente!')
        elif ano2 > ano1 or mes2 > mes1 or dia2 > dia1:
            print('\nA segunda data é mais recente')
        else:
            print('\nAs datas digitadas são iguais')
    else:
        print('\nAlguma das datas digitadas é inválida! Revise os valores')
        main()

main()

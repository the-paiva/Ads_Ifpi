#Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar 
#outro valor, deve aparecer valor inválido.

from Utils.io_utils import pedir_int

#Verifica se o número digitado pelo usuário é válido
def eh_valor_valido(num):
    if num >= 1 and num <= 7:
        return True
    
    return False

#Retorna o dia da semana correspondente ao número digitado pelo usuário
def retornar_dia_da_semana(num):
    if num == 1:
        return 'Domingo'
    elif num == 2:
        return 'Segunda'
    elif num == 3:
        return 'Terça'
    elif num == 4:
        return 'Quarta'
    elif num == 5:
        return 'Quinta'
    elif num == 6:
        return 'Sexta'
    
    return 'Sábado'

def main():
    num = pedir_int('\nDigite um número de 1 a 7 para retornar um dia da semana: ')

    if eh_valor_valido(num):
        dia_da_semana = retornar_dia_da_semana(num)
        print(f'\n{num} - {dia_da_semana}')
    else:
        print(f'\nVALOR INVÁLIDO!')

main()

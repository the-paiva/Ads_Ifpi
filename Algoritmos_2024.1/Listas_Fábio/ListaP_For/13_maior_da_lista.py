#Leia N e uma lista de N números e escreva o maior número da lista.

from Utils.io_utils import pedir_int_min, pedir_float
from Utils.math_utils import eh_maior

def main():
    quant_num = pedir_int_min('Digite quantos números terão na lista (Mínimo 2): ', 2)

    for cont in range(1, quant_num + 1):
        num = pedir_float(f'Digite o {cont}º número: ')

        #Horrendo, eu sei
        if cont == 1:
            maior_num = num
        elif eh_maior(num, maior_num):
            maior_num = num

    print(f'\nMaior número digitado: {maior_num:.2f}')

main()

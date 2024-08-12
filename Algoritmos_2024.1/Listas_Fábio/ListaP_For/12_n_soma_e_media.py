#Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

from Utils.io_utils import pedir_float, pedir_int_min
from Utils.math_utils import calcular_media_aritmetica

def main():
    quant_num = pedir_int_min('Digite quantos números terão na sequência: ', 2)
    soma = 0

    for cont in range(quant_num):
        num = pedir_float(f'Digite o {cont + 1}º número: ')
        soma += num

    media = calcular_media_aritmetica(soma, quant_num)

    print(f'\nSoma dos números: {soma:.2f}')
    print(f'Média dos números: {media:.2f}')

main()

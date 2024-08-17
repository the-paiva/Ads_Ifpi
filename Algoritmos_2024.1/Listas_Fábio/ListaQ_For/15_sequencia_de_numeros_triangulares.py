#Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

from Utils.io_utils import pedir_int_min

#Calcula o termo atual da sequência de acordo com a fórmula da sequência de números triangulares
def calcular_termo_triangular(cont):
    return cont * (cont + 1) / 2

def main():
    n = pedir_int_min('Digite o número de termos da sequência: ', 1)
    termo_triangular = 1

    print('\nSEQUÊNCIA')

    for cont in range(1, n + 1):
        termo_triangular = calcular_termo_triangular(cont)
        print(f'{termo_triangular:.0f}')

main()

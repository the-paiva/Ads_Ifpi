#Leia N e escreva todos os números inteiros pares de 1 a N.

from Utils.io_utils import pedir_int_min
from Utils.math_utils import eh_par

def main():
    n = pedir_int_min('Digite um número inteiro (Acima de 1): ', 2)
    print('\nSequência de números')

    for cont in range(1, n + 1):
        if eh_par(cont):
            print(cont)

main()

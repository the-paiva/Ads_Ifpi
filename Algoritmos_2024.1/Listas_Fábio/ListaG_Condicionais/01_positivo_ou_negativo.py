#Leia um número e mostre na tela se o número é positivo ou negativo.

from Utils.io_utils import pedir_int_restrito
from Utils.math_utils import eh_positivo

def main():
    num = pedir_int_restrito('\nDigite um número inteiro diferente de 0: ', 0)

    if eh_positivo(num):
        print(f'\n{num} é um número positivo!')
    else:
        print(f'\n{num} é um número negativo!')

main()

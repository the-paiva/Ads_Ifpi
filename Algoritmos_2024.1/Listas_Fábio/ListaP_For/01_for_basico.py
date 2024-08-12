#Leia N e escreva todos os números inteiros de 1 a N.

from Utils.io_utils import pedir_int_min

def main():
    n = pedir_int_min('Digite um número inteiro (Acima de 1): ', 2)
    print('\nSequência de números')

    for cont in range(1, n + 1):
        print(cont)

main()

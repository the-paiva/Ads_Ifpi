#Leia um número, calcule e escreva seu fatorial.

from Utils.io_utils import pedir_int_min

def main():
    num = pedir_int_min('Digite um número inteiro positivo: ', 0)
    fatorial = num

    print('\nFatorial')
    print(num, end='')

    for cont in range (num - 1, 0, -1):
        print(f' x {cont}', end='')
        fatorial *= cont

    print(f' = {fatorial}')

main()

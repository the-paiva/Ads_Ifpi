#Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

from Utils.io_utils import pedir_int_min

#Soma todos os números entre 1 e o número digitado pelo usuário (n)
def calcular_somatorio(n):
    somatorio = 0

    for cont in range(1, n + 1):
        somatorio += cont

    return somatorio

def main():
    n = pedir_int_min('Digite um número inteiro (Acima de 1): ', 2)
    somatorio = calcular_somatorio(n)
    print(f'Somatório de 1 até {n}: {somatorio}')

main()

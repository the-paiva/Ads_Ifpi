#Leia N, calcule e escreva o valor de S.
#S = 1/n - n-1/2 + 3/n-2... +- n/1

from Utils.io_utils import pedir_int_min

#Calcula o somatório de acordo com a sequência fornecida
def calcular_somatorio(n):
    somatorio = 0

    for cont in range(1, n + 1):
        termo = 1 / (n - cont + 1)

        if cont % 2 == 0:
            somatorio -= termo
        else:
            somatorio += termo

    return somatorio

#Escreve o resultado do somatório
def mostrar_resultado(somatorio):
    print('\nExemplo de sequência: S = 1/3 - 2/2 + 3/1')
    print(f'Valor do somatório da sequência atual: {somatorio:.2f}')

def main():
    n = pedir_int_min('Digite um número inteiro maior que 0: ', 1)

    somatorio = calcular_somatorio(n)

    mostrar_resultado(somatorio)

main()

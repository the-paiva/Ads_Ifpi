#Leia N, calcule e escreva o valor de S.
#S = 1/n + 2/n-1 + 3/n-2... + n/1

from Utils.io_utils import pedir_int_min

#Calcula o somatório de acordo com a sequência fornecida
def calcular_somatorio(n):
    somatorio = 0

    for cont in range(n, 0, -1):
        somatorio += 1 / cont

    return somatorio

#Escreve o resultado do somatório
def mostrar_resultado(somatorio):
    print('\nExemplo de sequência: S = 1/10 + 2/9 + 3/8... 10/1')
    print(f'Valor do somatório da sequência atual: {somatorio:.2f}')

def main():
    n = pedir_int_min('Digite um número inteiro maior que 0: ', 1)

    somatorio = calcular_somatorio(n)

    mostrar_resultado(somatorio)

main()

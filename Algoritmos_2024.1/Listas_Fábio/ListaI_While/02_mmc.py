#Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.

from Utils.io_utils import pedir_int

#Calcula o mdc de dois números
def calcular_mdc(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1

#Calcula o mmc de dois números
def calcular_mmc(num1, num2, mdc):
    return (num1 * num2) / mdc

def main():
    #Entrada
    num1 = pedir_int('\nDigite o primeiro número: ')
    num2 = pedir_int('Digite o segundo número: ')

    #Processamento
    mdc = calcular_mdc(num1, num2)
    mmc = calcular_mmc(num1, num2, mdc)

    #Saída
    print(f'\nO mmc de {num1} e {num2} é {mmc:.0f}')

main()

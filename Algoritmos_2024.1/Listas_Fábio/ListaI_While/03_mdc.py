#Leia 2 (dois) números, calcule e escreva o mdc (máximo divisor comum) entre os números lidos.

from Utils.io_utils import pedir_int

#Calcula o mdc de dois números
def calcular_mdc(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1

def main():
    #Entrada
    num1 = pedir_int('\nDigite o primeiro número: ')
    num2 = pedir_int('Digite o segundo número: ')

    #Processamento
    mdc = calcular_mdc(num1, num2)

    #Saída
    print(f'\nO mdc de {num1} e {num2} é {mdc:.0f}')

main()

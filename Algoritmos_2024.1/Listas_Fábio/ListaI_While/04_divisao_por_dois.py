#Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
#resultado da última divisão efetuada.

from Utils.io_utils import pedir_int

#Divide um número por 2 sucessivamente
def dividir_sucessivo(num):
    while num >= 1:
        num = dividir_sucessivo(num / 2)

    return num

def main():
    #Entrada
    num = pedir_int('\nDigite o primeiro número: ')

    #Processamento
    num = dividir_sucessivo(num)

    #Saída
    print(f'\nO resultado final das divisões é {num}')

main()

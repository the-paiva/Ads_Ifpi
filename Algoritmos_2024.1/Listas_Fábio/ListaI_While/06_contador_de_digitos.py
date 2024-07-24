#Escreva um algoritmo para determinar o número de dígitos de um número informado.

from Utils.io_utils import pedir_int

#Retorna a quantidade de dígitos de um número
def retornar_digitos(num):
    digitos = 0

    while num != 0:
        num = num // 10
        digitos += 1

    return digitos

def main():
    num = pedir_int('\nDigite um número inteiro: ')

    if num < 0:
        num *= -1 #Converte em número positivo

    digitos = retornar_digitos(num)

    print(f'\nQuantidade de dígitos: {digitos}')

main()

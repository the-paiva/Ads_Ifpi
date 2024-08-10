#Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
#de divisão (/ e %) sejam utilizados.

from Utils.io_utils import pedir_int, pedir_int_restrito

#Realiza a divisão de dois números sem utilizar os operadores da divisão
def dividir(dividendo, divisor):
    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        quociente += 1

    return quociente, resto

def main():
    dividendo = pedir_int('\nDigite um número inteiro para ser o dividendo: ')
    divisor = pedir_int_restrito('Agora digite um número inteiro para ser o divisor (com exceção de 0): ', 0)
    
    quociente, resto = dividir(dividendo, divisor)

    print(f'\nQuociente: {quociente}')
    print(f'Resto: {resto}')

main()

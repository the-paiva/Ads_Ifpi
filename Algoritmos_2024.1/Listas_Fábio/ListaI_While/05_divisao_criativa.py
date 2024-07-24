#Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
#divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
#chegar a 2.

from Utils.io_utils import pedir_int

#Faz a divisão das variáveis x e n
def dividir_xn(x, n):
    return x / n, n - 1

#Mostra os valores de x e n
def mostrar_valores_xn(x, n):
    print(f'\nValor atual de x: {x}')
    print(f'Valor atual de n: {n}')

#Mostra a mensagem de encerramento do programa
def encerrar():
    print('Encerrando o programa...')

def main():
    #Entrada
    x = pedir_int('\nDigite o primeiro número (x): ')
    n = pedir_int('Digite o segundo número (n): ')

    #Processamento
    while n > 2:
        x, n = dividir_xn(x, n)

        #Saída - Parte 1
        mostrar_valores_xn(x, n)

    #Saída - Parte 2
    encerrar()

main()

#Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
#(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

from Utils.io_utils import pedir_int_min

#Escreve a condição inicial da sequência (que F(0) = 0 e F(1) = 1)
def escrever_condicao_inicial():
    print('\nSEQUÊNCIA DE FIBONACCI')
    print('F(0) = 0')
    print('F(1) = 1')

#Calcula o termo atual de acordo com a fórmula da sequência de Fibonacci
def calcular_termo_fibonacci(termo_anterior, termo_retrasado):
    return termo_anterior + termo_retrasado

def main():
    n = pedir_int_min('-> Digite a quantidade de termos da sequência (Mínimo 2): ', 2)

    escrever_condicao_inicial()
    termo_retrasado = 0
    termo_anterior = 1

    for cont in range(2, n + 1):
        termo_atual = calcular_termo_fibonacci(termo_anterior, termo_retrasado)
        print(f'F({cont}) = {termo_atual}') #Ex: F(2) = 1

        termo_retrasado = termo_anterior
        termo_anterior = termo_atual

main()

#Leia uma lista de números e que para cada número lido, escreva o próprio número e a relação de seus
#divisores. (flag número = 0).

from time import sleep
from Utils.io_utils import pedir_int

#Verifica a divisibilidade de um número pelo outro
def eh_divisor(num1, num2):
    if num1 % num2 == 0:
        return True
    
    return False

#Escreve o divisor na tela
def escrever_divisor(divisor):
    print(divisor)

#Agregador de funções relacionadas à analise de divisibilidade de um número
def analisar_divisibilidade(num):
    count = 1

    print('')

    while count <= num:
        divisor = eh_divisor(num, count)

        if divisor:
            escrever_divisor(count)

        count += 1

#Mensagem de encerramento do programa
def encerrar():
    print('\nEncerrando o programa...')
    sleep(2.5)

def main():
    while True:
        num = pedir_int('\nDigite um número (0 para encerrar o programa): ')

        if num == 0:
            break

        analisar_divisibilidade(num)
    
    encerrar()

main()

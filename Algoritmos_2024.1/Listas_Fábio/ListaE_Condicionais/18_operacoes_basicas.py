#Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma:
#1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa 
#operação sobre os dois valores lidos.

from time import sleep

#Pede um valor float
def pedir_float(texto):
    return float(input(texto))

#Pede um valor int
def pedir_int(texto):
    return int(input(texto))

#Verifica se a operação digitada pelo usuário é válida
def eh_operacao_valida(cod_operacao, num2):
    if cod_operacao == 1 or cod_operacao == 2 or cod_operacao == 3 or (cod_operacao == 4 and num2 != 0):
        return True
    
    return False

#Atribui o sinal da operação escolhida a uma string
def atribuir_sinal(cod_operacao):
    if cod_operacao == 1:
        return '+'
    elif cod_operacao == 2:
        return '-'
    elif cod_operacao == 3:
        return '*'
    else:
        return '/'

#Realiza o cálculo dos números de acordo com a operação escolhida
def calcular_numeros(cod_operacao, num1, num2):
    if cod_operacao == 1:
        return num1 + num2
    elif cod_operacao == 2:
        return num1 - num2
    elif cod_operacao == 3:
        return num1 * num2
    else:
        return num1 / num2

#Descreve as instruções de uso do programa
def escrever_instrucoes():
    print('')
    print('-' * 50)
    print('Digite 1 para adição')
    print('Digite 2 para subtração')
    print('Digite 3 para multiplicação')
    print('Digite 4 para divisão')
    print('-' * 50)

#Escreve o resultado do cálculo realizado - Exemplo: 5 + 3 = 8
def escrever_resultado(num1, sinal, num2, resultado):
    print(f'\n{num1:.2f} {sinal} {num2:.2f} = {resultado:.2f}')

#Encerra o programa com uma mensagem de erro
def erro():
    print('\nOPERAÇÃO INVÁLIDA! Encerrando o programa...')
    sleep(3)

def main():
    num1 = pedir_float('\nDigite o primeiro número: ')
    num2 = pedir_float('Digite o segundo número: ')
    
    escrever_instrucoes()
    cod_operacao = pedir_int('-> ')

    if eh_operacao_valida(cod_operacao, num2):
        sinal = atribuir_sinal(cod_operacao)
        resultado = calcular_numeros(cod_operacao, num1, num2)
        escrever_resultado(num1, sinal, num2, resultado)
    else:
        erro()

main()

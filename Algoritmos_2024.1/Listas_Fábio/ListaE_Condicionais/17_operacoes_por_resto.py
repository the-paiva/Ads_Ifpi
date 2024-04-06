#Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

from time import sleep

#Pede um valor int
def pedir_int(texto):
    return int(input(texto))

#Verifica se uma divisão tem resto 1
def eh_resto1(num1, num2):
    if num1 % num2 == 1:
        return True
    
    return False

#Verifica se uma divisão tem resto 2
def eh_resto2(num1, num2):
    if num1 % num2 == 2:
        return True
    
    return False

#Verifica se uma divisão tem resto 3
def eh_resto3(num1, num2):
    if num1 % num2 == 3:
        return True
    
    return False

#Verifica se uma divisão tem resto 4
def eh_resto4(num1, num2):
    if num1 % num2 == 4:
        return True
    
    return False

#Verifica se um número é par ou ímpar, retornando o tipo em uma string
def verificar_tipo_num(num):
    if num % 2 == 0:
        return 'PAR'
    
    return 'ÍMPAR'

#Verifica se o divisor de uma operação é válido (Diferente de zero)
def eh_divisor_valido(num2):
    if num2 != 0:
        return True
    
    return False

#Realiza as operações do caso em que o resto da divisão for 1
def calcular_resto1(num1, num2):
   return num1 + num2 + 1

#Realiza as operações do caso em que o resto da divisão for 3
def calcular_resto3(num1, num2):
    return num1 * (num1 + num2)

#Realiza as operações do caso em que o resto da divisão for 4
def calcular_resto4(num1, num2):
    return (num1 + num2) / num2

#Mostra o resultado do caso em que o resto da divisão for 1
def mostrar_resultado_resto1(num1, num2, resultado):
    print('\nResto: 1')
    print(f'Operação: {num1} + {num2} + 1 = {resultado}')

#Mostra o resultado do caso em que o resto da divisão for 2
def mostrar_resultado_resto2(num1, num2, tipo_num1, tipo_num2):
    print('\nResto: 2')
    print(f'{num1} é um número {tipo_num1}')
    print(f'{num2} é um número {tipo_num2}')

#Mostra o resultado do caso em que o resto da divisão for 3
def mostrar_resultado_resto3(num1, num2, resultado):
    print('\nResto: 3')
    print(f'Operação: {num1} x ({num1} + {num2}) = {resultado}')

#Encerra o programa com uma mensagem de erro por divisor inválido
def erro_divisor_invalido():
    print('\nDIVISOR INVÁLIDO! Encerrando o programa...')
    sleep(3)

#Mostra o resultado do caso em que o resto da divisão for 4
def mostrar_resultado_resto4(num1, num2, resultado):
    print('\nResto: 4')
    print(f'Operação: ({num1} + {num2}) / {num2} = {resultado:.2f}')

#Mostra o resultado dos casos gerais não especificados
def mostrar_resultado_generico(num1, num2, resto, quadrado_num1, quadrado_num2):
    print(f'\nResto = {resto}')
    print(f'Quadrado de {num1} = {quadrado_num1}')
    print(f'Quadrado de {num2} = {quadrado_num2}')

def main():
    num1 = pedir_int('\nDigite o primeiro número: ')
    num2 = pedir_int('Digite o segundo número: ')

    if eh_divisor_valido(num2):
        if eh_resto1(num1, num2):
            resultado = calcular_resto1(num1, num2)
            mostrar_resultado_resto1(num1, num2, resultado)
        elif eh_resto2(num1, num2):
            tipo_num1 = verificar_tipo_num(num1)
            tipo_num2 = verificar_tipo_num(num2)
            mostrar_resultado_resto2(num1, num2, tipo_num1, tipo_num2)
        elif eh_resto3(num1, num2):
            resultado = calcular_resto3(num1, num2)
            mostrar_resultado_resto3(num1, num2, resultado)
        elif eh_resto4(num1, num2):
            resultado = calcular_resto4(num1, num2)
            mostrar_resultado_resto4(num1, num2, resultado)
        else:
            resto = num1 % num2
            quadrado_num1 = num1**2
            quadrado_num2 = num2**2
            mostrar_resultado_generico(num1, num2, resto, quadrado_num1, quadrado_num2)
    else:
        erro_divisor_invalido()

main()

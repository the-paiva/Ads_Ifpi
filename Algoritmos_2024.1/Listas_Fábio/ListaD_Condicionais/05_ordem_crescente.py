#Leia 3 (três) números e escreva-os em ordem crescente.

#Pede um número do tipo float
def pedir_float(texto):
    num = float(input(texto))
    return num

#Compara dois números para saber qual é maior
def comparar_numeros(num1, num2):
    if num1 > num2:
        aux_num = num2
        num2 = num1
        num1 = aux_num

    return num1, num2

#Saída de dados do programa
def mostrar_resultado(num1, num2, num3):
    print(f'\nEm ordem crescente: {num1:.2f}; {num2:.2f}; {num3:.2f}')

def main():
    #Entrada
    num1 = pedir_float('\nDigite o primeiro número: ')
    num2 = pedir_float('Digite o segundo número: ')
    num3 = pedir_float('Digite o terceiro número: ')

    #Processamento
    num1, num2 = comparar_numeros(num1, num2)
    num2, num3 = comparar_numeros(num2, num3)
    num1, num2 = comparar_numeros(num1, num2)

    #Saída
    mostrar_resultado(num1, num2, num3)

main()

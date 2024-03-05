#Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

#Entrada de um número de tipo float
def get_float(texto):
    num = float(input(texto))
    return num

#Retorna a quantidade de números iguais
def checar_iguais(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return 3
    elif num1 == num2 or num2 == num3:
        return 2
    else:
        return 0
    
def mostrar_resultado(num_iguais):
    if num_iguais > 0:
        print(f'\nQuantidade de números iguais: {num_iguais}')
    else:
        print('\nTodos os números são diferentes entre si.')

def main():
    #Entrada
    num1 = get_float('\nDigite o primeiro número: ')
    num2 = get_float('Digite o segundo número: ')
    num3 = get_float('Digite o terceiro número: ')

    #Processamento
    num_iguais = checar_iguais(num1, num2, num3)

    #Saída
    mostrar_resultado(num_iguais)

main()

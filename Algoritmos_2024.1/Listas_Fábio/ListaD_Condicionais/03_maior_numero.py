#Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

#Entrada de um número do tipo float
def pedir_float(texto):
    num = float(input(texto))
    return num

#Verifica se os números são todos iguais
def eh_igual(num1, num2, num3):
    if (num1 == num2 == num3):
        return True
    else:
        return False

#Verifica qual é o maior número
def checar_maior_numero(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        maior = num1
    elif (num2 > num1 and num2 > num3):
        maior = num2
    elif (num3 > num1 and num3 > num2):
        maior = num3

    return maior

#Saída de dados do programa
def mostrar_resultado(maior, igual):
    if (not igual):
        print(f'\nMaior número digitado: {maior}')
    else:
        print('\nOs números digitados são iguais!')

def main():
    #Entrada
    num1 = pedir_float('\nDigite o primeiro número: ')
    num2 = pedir_float('Digite o segundo número: ')
    num3 = pedir_float('Digite o terceiro número: ')

    #Processamento
    igual = eh_igual(num1, num2, num3)

    if (not igual):
        maior = checar_maior_numero(num1, num2, num3)
    else:
        maior = 0

    #Saída
    mostrar_resultado(maior, igual)

main()

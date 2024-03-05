#Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

#Pede um número do tipo Float
def pedir_float(texto):
    num = float(input(texto))
    return num

#Verifica se dois números são iguais
def eh_igual(num1, num2):
    if (num1 == num2):
        return True
    else:
        return False

#Verifica qual é o maior e qual é o menor entre dois números  
def checar_maior_e_menor(num1, num2):
    if (num1 > num2):
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    return maior, menor

#Saída de dados do programa
def print_resultado(igual, maior, menor):
    if (igual):
        print('\nOs dois números são iguais!')
    else:
        print(f'\nMaior número: {maior:.2f}\nMenor número: {menor:.2f}')

def main():
    #Entrada
    num1 = pedir_float('\nDigite o 1º número: ')
    num2 = pedir_float('Digite o 2º número: ')

    #Processamento
    igual = eh_igual(num1, num2)

    if (not igual):
        maior, menor = checar_maior_e_menor(num1, num2)
    else:
        maior, menor = 0, 0

    #Saída
    print_resultado(igual, maior, menor)

main()

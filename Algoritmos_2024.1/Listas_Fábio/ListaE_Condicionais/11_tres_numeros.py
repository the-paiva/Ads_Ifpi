#Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

from time import sleep

#Pede um valor int
def pedir_int(texto):
    return int(input(texto))

#Verifica se o valor de opcao é válido
def eh_opcao_valida(opcao):
    if opcao == 1 or opcao == 2 or opcao == 3:
        return True
    
    return False

#Retorna o número da opção escolhida pelo usuário
def atribuir_opcao_escolhida(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    else:
        return num3

#Escreve o enunciado que antecede o pedido de opcao
def escrever_enunciado():
    print('-' * 50)
    print('Você digitou três números')
    print('Digite 1 para escrever o valor do primeiro número')
    print('Digite 2 para escrever o valor do segundo número')
    print('Digite 3 para escrever o valor do terceiro número')
    print('-' * 50)

#Encerra o programa com uma mensagem de erro
def erro():
    print('\nVALOR INVÁLIDO! Encerrando o programa...')
    sleep(3)

def main():
    num1 = pedir_int('\nDigite o valor do primeiro número: ')
    num2 = pedir_int('Digite o valor do segundo número: ')
    num3 = pedir_int('Digite o valor do terceiro número: ')
    
    escrever_enunciado()
    opcao = pedir_int('-> ')

    if eh_opcao_valida(opcao):
        opcao_escolhida = atribuir_opcao_escolhida(opcao, num1, num2, num3)
        print(opcao_escolhida)
    else:
        erro()

main()

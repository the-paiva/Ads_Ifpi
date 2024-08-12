#Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

from Utils.io_utils import pedir_int_min

#Verifica se um número é múltiplo de outro
def eh_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    
    return False

def main():
    num = pedir_int_min('Digite um número inteiro positivo: ', 1)
    limite_inferior = pedir_int_min('Digite o limite inferior: ', num)
    limite_superior = pedir_int_min('Digite o limite superior: ', limite_inferior + 1)

    print(f'\nMúltiplos de {num}')

    for cont in range(limite_inferior, limite_superior + 1):
        if eh_multiplo(cont, num):
            print(cont)

main()

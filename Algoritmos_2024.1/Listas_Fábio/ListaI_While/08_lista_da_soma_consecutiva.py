#Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da 
#lista ocorrendo quando a soma de dois números consecutivos da lista for igual a X.

from Utils.io_utils import pedir_int

def main():
    num_procurado = pedir_int('Digite um número para ser procurado: ')
    num_anterior = 0
    soma = num_procurado + 1
    
    while num_procurado != soma:
        num_atual = pedir_int('\nDigite um número inteiro: ')
        soma = num_atual + num_anterior
        print(f'{num_anterior} + {num_atual} = {soma}')

        num_anterior = num_atual

    print('\nO número procurado foi encontrado!')

main()

#Escreva um algoritmo que leia a razão de uma PA (Progressão Aritmética) e o seu primeiro termo e
#escreva os N termos da PA. Ler o valor de N.

from Utils.io_utils import pedir_float, pedir_int

def main():
    primeiro_termo = pedir_float('Digite o primeiro termo da PA: ')
    razao = pedir_float('Digite a razão da PA: ')
    n = pedir_int('Digite o número de termos que deseja calcular (N): ')

    cont = 0
    termo_atual = primeiro_termo
    print('\n============================================')

    while cont < n:
        print(f'Termo {cont + 1}: {termo_atual}')
        termo_atual += razao
        cont += 1

main()

#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
#Aritmética que tem por valor inicial A0 e razão R.

from Utils.io_utils import pedir_int_min

def main():
    valor_inicial = pedir_int_min('Digite o valor inicial (A0): ', 1)
    limite = pedir_int_min('Digite o limite: ', valor_inicial + 1)
    razao = pedir_int_min('Digite a razão (R): ', 1)

    print('\nSequência de números')

    for termo in range(valor_inicial, limite, razao):
        print(termo)

main()

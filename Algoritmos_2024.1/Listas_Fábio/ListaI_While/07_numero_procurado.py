#Leia um número e, a seguir, leia uma lista de números até achar um igual ao
#primeiro número lido.

from Utils.io_utils import pedir_int

def main():
    num_procurado = pedir_int('Digite um número inteiro para ser procurado: ')
    num_atual = num_procurado + 1

    while num_procurado != num_atual:
        num_atual = pedir_int('\nDigite um número inteiro qualquer: ')

    print('O número procurado foi encontrado!')

main()

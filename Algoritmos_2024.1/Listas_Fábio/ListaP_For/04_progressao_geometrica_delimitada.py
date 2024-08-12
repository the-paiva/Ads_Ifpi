#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
#Geométrica que tem por valor inicial A0 e razão R.

from Utils.io_utils import pedir_int_min

def main():
    valor_inicial = pedir_int_min('Digite o valor inicial (A0): ', 1)
    limite = pedir_int_min('Digite o limite: ', valor_inicial + 1)
    razao = pedir_int_min('Digite a razão (R): ', 1)

    print('\nSequência de números')

    termo = valor_inicial

    for cont in range(limite):
        if termo >= limite:
            break
        
        print(termo)
        termo *= razao

main()

#Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*)
#seja utilizado.

from Utils.io_utils import pedir_int

#Multiplica os fatores e atribui o resultado em variável inteira
def multiplicar_fatores(fator1, fator2, produto):
    cont = 0
    
    if fator2 >= 0:
        while cont < fator2:
            produto += fator1
            cont += 1
    else:
        while cont > fator2:
            produto -= fator1
            cont -= 1

    return produto

def main():
    fator1 = pedir_int('Digite um número inteiro: ')
    fator2 = pedir_int('Agora digite outro número inteiro: ')
    produto = 0

    produto = multiplicar_fatores(fator1, fator2, produto)

    print(f'{fator1} x {fator2} = {produto}')

main()

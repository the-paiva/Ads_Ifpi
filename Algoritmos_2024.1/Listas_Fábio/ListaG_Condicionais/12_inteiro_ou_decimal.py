#Leia um número e escreva se o número é inteiro ou decimal.

from Utils.io_utils import pedir_float

#Verifica se um número é inteiro
def eh_inteiro(num):
    if num - int(num) == 0:
        return True
    
    return False

def main():
    num = pedir_float('\nDigite um número: ')

    if eh_inteiro(num):
        print(f'\n{num:.0f} é um número inteiro.')
    else:
        print(f'\n{num:.2f} é um número decimal.')

main()

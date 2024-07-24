#Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
#e na base hexadecimal.

from Utils.io_utils import pedir_int_min_max

#Converte um número da base decimal para binário
def converter_para_binario(num):
    num_bin = ''
    
    while num > 0:
        resto = num % 2
        num_bin = str(resto) + num_bin
        num //= 2

    if num_bin == '':
        num_bin = '0'

    return num_bin

#Converte um número da base decimal para hexadecimal
def converter_para_hexadecimal(num):
    num_hex = ''

    while num > 0:
        resto = num % 16

        if resto == 10:
            num_hex = 'A' + num_hex
        elif resto == 11:
            num_hex = 'B' + num_hex
        elif resto == 12:
            num_hex = 'C' + num_hex
        elif resto == 13:
            num_hex = 'D' + num_hex
        elif resto == 14:
            num_hex = 'E' + num_hex
        elif resto == 15:
            num_hex = 'F' + num_hex
        else:
            num_hex = str(resto) + num_hex
            
        num //= 16

    if num_hex == '':
        num_hex = '0'

    return num_hex

#Mostra o resultado das conversões feitas
def mostrar_conversoes(num_bin, num_hex):
    print(f'\nEm binário: {num_bin}')
    print(f'Em hexadecimal: {num_hex}')

def main():
    num = pedir_int_min_max('Escreva um número na base decimal (entre 0 e 255): ', 0, 255)

    num_bin = converter_para_binario(num)
    num_hex = converter_para_hexadecimal(num)

    mostrar_conversoes(num_bin, num_hex)

main()

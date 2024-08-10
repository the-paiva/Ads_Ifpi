#Escreva um algoritmo que leia um número decimal (até 3 dígitos) e escreva o seu equivalente em
#numeração romana. Utilize funções para obter cada dígito do número decimal e para a transformação
#de numeração decimal para romana (Dica: 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M).

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import dividir_centena

#Converte um dígito para seu correspondente romano
def digito_para_romano(digito, unidade, cinco, dez):
    if digito == 1:
        return unidade
    elif digito == 2:
        return unidade * 2
    elif digito == 3:
        return unidade * 3
    elif digito == 4:
        return unidade + cinco
    elif digito == 5:
        return cinco
    elif digito == 6:
        return cinco + unidade
    elif digito == 7:
        return cinco + unidade * 2
    elif digito == 8:
        return cinco + unidade * 3
    elif digito == 9:
        return unidade + dez
    else:
        return ""

#Concatena dígitos em algarismo romano para formar um número inteiro
def converter_para_romano(centena, dezena, unidade):
    romano = ""

    if centena > 0:
        romano += digito_para_romano(centena, "C", "D", "M")

    if dezena > 0:
        romano += digito_para_romano(dezena, "X", "L", "C")

    if unidade > 0:
        romano += digito_para_romano(unidade, "I", "V", "X")
    
    return romano

def main():
    num = pedir_int_min_max('Digite um número decimal (1 a 999): ', 1, 999)

    centena, dezena, unidade = dividir_centena(num)
    romano = converter_para_romano(centena, dezena, unidade)

    print(f'O número {num} em algarismo romano é: {romano}')

main()

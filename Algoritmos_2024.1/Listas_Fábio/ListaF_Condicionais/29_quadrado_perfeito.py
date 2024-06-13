#Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
#formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
#Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import dividir_milhar, eh_igual

#Calcula a raíz quadrada de um número
def calcular_raiz_quadrada(num):
    return num**0.5

#Escreve os cálculos que foram feitos no programa
def escrever_calculos(primeira_dezena, segunda_dezena, soma_de_dezenas, raiz_quadrada):
    print(f'''\n=============== CÁLCULOS ===============
    Primeira dezena: {primeira_dezena}
    Segunda dezena: {segunda_dezena}
    Soma das dezenas: {soma_de_dezenas}
    Raíz quadrada: {raiz_quadrada:.2f}\n''')

def main():
    num = pedir_int_min_max('\nDigite um número de 4 dígitos: ', 1000, 9999)
    raiz_quadrada = calcular_raiz_quadrada(num)
    
    milhar, centena, dezena, unidade = dividir_milhar(num)
    primeira_dezena = int(str(milhar) + str(centena))
    segunda_dezena = int(str(dezena) + str(unidade))
    soma_de_dezenas = primeira_dezena + segunda_dezena

    escrever_calculos(primeira_dezena, segunda_dezena, soma_de_dezenas, raiz_quadrada)

    if eh_igual(raiz_quadrada, soma_de_dezenas):
        print(f'{num} é um quadrado perfeito!')
    else:
        print(f'{num} não é um quadrado perfeito!')

main()

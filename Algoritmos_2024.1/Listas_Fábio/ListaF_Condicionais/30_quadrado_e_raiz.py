#Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica:
#Se dividirmos o número em dois números de dois dígitos, um composto pela dezena e pela unidade, 
#e outro pelo milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, 
#o quadrado deste terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
#2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45**2 = 2025.

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import dividir_milhar, eh_igual

#Escreve os cálculos realizados
def escrever_calculos(num, primeira_dezena, segunda_dezena, soma_de_dezenas, quadrado):
    print(f'''\n=============== CÁLCULOS ===============
    Número original: {num}
    Primeira dezena: {primeira_dezena}
    Segunda dezena: {segunda_dezena}
    Soma das dezenas: {soma_de_dezenas}
    Quadrado: {soma_de_dezenas}**2 = {quadrado}''')
    print('=' * 40)

def main():
    num = pedir_int_min_max('\nDigite um número de 4 dígitos: ', 1000, 9999)

    milhar, centena, dezena, unidade = dividir_milhar(num)
    primeira_dezena = int(str(milhar) + str(centena))
    segunda_dezena = int(str(dezena) + str(unidade))
    soma_de_dezenas = primeira_dezena + segunda_dezena
    quadrado = soma_de_dezenas ** 2

    escrever_calculos(num, primeira_dezena, segunda_dezena, soma_de_dezenas, quadrado)

    if eh_igual(quadrado, num):
        print(f'\nO quadrado de {soma_de_dezenas} é igual ao número original digitado')
    else:
        print(f'\nO quadrado de {soma_de_dezenas} é diferente do número original digitado')

main()

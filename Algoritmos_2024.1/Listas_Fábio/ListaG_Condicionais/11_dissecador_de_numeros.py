#Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
#número. Observando os termos no plural a colocação do "e", da vírgula entre outros. 
#Exemplos:
#* 326 = 3 centenas, 2 dezenas e 6 unidades
#* 12 = 1 dezena e 2 unidades

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import dividir_centena, dividir_dezena

#Coloca uma palavra no plural caso a quantidade de elementos que a acompanha seja maior do que 1
def acrescentar_plural(elemento_analisado, quant_elementos):
    if quant_elementos > 1:
        return elemento_analisado + 's'
    
    return elemento_analisado

def main():
    NUM_MINIMO = 1
    NUM_MAXIMO = 999
    num = pedir_int_min_max('\nDigite um número 1 e 999: ', NUM_MINIMO, NUM_MAXIMO)

    str_centena = 'centena'
    str_dezena = 'dezena'
    str_unidade = 'unidade'

    print(f'\n{num} = ', end='')

    if num >= 100:
        centena, dezena, unidade = dividir_centena(num)

        str_centena = acrescentar_plural(str_centena, centena)
        str_dezena = acrescentar_plural(str_dezena, dezena)
        str_unidade = acrescentar_plural(str_unidade, unidade)

        #Ex: 231 = 2 centenas, 3 dezenas e 1 unidade
        print(f'{centena} {str_centena}, {dezena} {str_dezena} e {unidade} {str_unidade}.')
    elif num >= 10:
        dezena, unidade = dividir_dezena(num)

        str_dezena = acrescentar_plural(str_dezena, dezena)
        str_unidade = acrescentar_plural(str_unidade, unidade)

        #Ex: 23 = 2 centenas e 3 unidades
        print(f'{dezena} {str_dezena} e {unidade} {str_unidade}.')
    else:
        str_unidade = acrescentar_plural(str_unidade, num)

        #Ex: 2 = 2 unidades
        print(f'{num} {str_unidade}.')

main()

#Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import eh_primo

def main():
    limite_inferior = pedir_int_min_max('Digite o Limite Inferior (Entre 1 e 99): ', 1, 99)
    limite_superior = pedir_int_min_max('Digite o Limite Superior (Entre limite superior e 100): ', limite_inferior + 1, 100)

    print('\nSequência de primos')

    for cont in range(limite_inferior, limite_superior + 1):
        if eh_primo(cont):
            print(cont)

main()

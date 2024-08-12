#Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

from Utils.io_utils import pedir_int_min
from Utils.math_utils import eh_par

def main():
    limite_inferior = pedir_int_min('Digite o Limite Inferior (Acima de 0): ', 1)
    limite_superior = pedir_int_min('Digite o Limite Superior (Acima do limite inferior): ', limite_inferior + 1)

    print('\nSequência de pares')

    for cont in range(limite_inferior, limite_superior + 1):
        if eh_par(cont):
            print(cont)

main()

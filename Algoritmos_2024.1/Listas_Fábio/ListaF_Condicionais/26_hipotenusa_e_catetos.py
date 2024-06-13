#Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

from Utils.io_utils import pedir_float_min
from Utils.math_utils import eh_triangulo, eh_igual

#Verifica qual foi o maior lado digitado pelo usuário
def verificar_maior_lado(lado1, lado2, lado3):
    if lado1 > lado2 and lado1 > lado3:
        return lado1, lado2, lado3
    elif lado2 > lado1 and lado2 > lado3:
        return lado2, lado1, lado3
    else:
        return lado3, lado1, lado2

#Saída de dados padrão do programa mostrando hipotenusa e catetos
def mostrar_resultado(maior_lado, lado_menor1, lado_menor2):
    print(f'\nHipotenusa: {maior_lado:.2f}')
    print(f'Catetos: {lado_menor1:.2f}; {lado_menor2:.2f}')

def main():
    lado1 = pedir_float_min('\nDigite o valor do primeiro lado do triângulo: ', 1)
    lado2 = pedir_float_min('Digite o valor do segundo lado do triângulo: ', 1)
    lado3 = pedir_float_min('Digite o valor do terceiro lado do triângulo: ', 1)

    if not (eh_igual(lado1, lado2) and eh_igual(lado2, lado3)):
        maior_lado, lado_menor1, lado_menor2 = verificar_maior_lado(lado1, lado2, lado3)
        
        if eh_triangulo(maior_lado, lado_menor1, lado_menor2):
            mostrar_resultado(maior_lado, lado_menor1, lado_menor2)
        else:
            print('\nOs lados digitados não formam um triângulo!')
    else:
        print('\nOs lados digitados não formam um triângulo!')

main()

#Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão
#a dois cantos de um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. 
#Lembre-se de que o valor da área não pode ser negativo.

from Utils.io_utils import pedir_float
from Utils.math_utils import calcular_modulo, eh_positivo

#Mostra uma mensagem de erro e reinicia o programa
def mostrar_erro():
    print('\nÁREA INVÁLIDA! Revise os valores digitados!')
    main()

def main():
    x = pedir_float('\nDigite o valor de X: ')
    y = pedir_float('Digite o valor de Y: ')
    area = calcular_modulo(x * y)

    if eh_positivo(area):
        print(f'\nÁrea do retângulo: {area:.2f}')
    else:
        mostrar_erro()

main()

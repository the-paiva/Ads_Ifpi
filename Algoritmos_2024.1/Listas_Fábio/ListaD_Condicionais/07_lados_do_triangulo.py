#Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

#Pede um número do tipo float
def pedir_float(texto):
    num = float(input(texto))
    return num

#Ordena os lados para descobrir qual é o maior
def ajustar_lados(lado1, lado2, lado3):
    if lado3 > lado2 and lado1 > lado3:
        return lado3, lado1, lado2
    elif lado2 > lado1 and lado2 > lado3:
        return lado2, lado1, lado3
    else:
        return lado1, lado2, lado3

#Verifica três lados para saber se formam um triângulo
def verificar_triangulo(maior_lado, lado_aux1, lado_aux2):
    if lado_aux1 + lado_aux2 >= maior_lado and maior_lado != 0 and lado_aux1 != 0 and lado_aux2 != 0:
        return True
    else:
        return False

#Verifica qual é o tipo de um triângulo de acordo com os seus lados
def verificar_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'equilátero'
    if lado1 != lado2 != lado3:
        return 'escaleno'
    else:
        return 'isósceles'

#Saída de dados do programa
def mostrar_resultado(eh_triangulo, tipo_triangulo):
    if eh_triangulo:
        print(f'\nOs três lados informados formam um triângulo {tipo_triangulo}.')
    else:
        print('\nOs três lados informados não formam um triângulo.')

def main():
    #Entrada
    lado1 = pedir_float('\nDigite o valor do primeiro lado: ')
    lado2 = pedir_float('Digite o valor do segundo lado: ')
    lado3 = pedir_float('Digite o valor do terceiro lado: ')

    #Processamento
    maior_lado, lado_aux1, lado_aux2 = ajustar_lados(lado1, lado2, lado3)
    eh_triangulo = verificar_triangulo(maior_lado, lado_aux1, lado_aux2) #lado_aux == lado_auxiliar

    if eh_triangulo:
        tipo_triangulo = verificar_tipo_triangulo(lado1, lado2, lado3)
    else:
        tipo_triangulo = '-'

    #Saída
    mostrar_resultado(eh_triangulo, tipo_triangulo)

main()

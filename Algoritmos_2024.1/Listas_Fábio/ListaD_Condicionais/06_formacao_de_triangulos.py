#Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

#Pede um número do tipo int
def pedir_int(texto):
    num = int(input(texto))
    return num

#Verifica se três ângulos formam um triângulo, retornando também o tipo de triângulo
def verificar_triangulo(angulo1, angulo2, angulo3):
    if angulo1 + angulo2 + angulo3 == 180 and angulo1 != 0 and angulo2 != 0 and angulo3 != 0:
        if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            return 'retângulo'
        elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            return 'acutângulo'
        else:
            return 'obtusângulo'
    else:
        return '-'

#Saída de dados do programa
def mostrar_resultado(tipo_triangulo):
    if tipo_triangulo != '-':
        print(f'\nOs três ângulos formam um triângulo {tipo_triangulo}.')
    else:
        print('\nOs três ângulos não formam um triângulo.')

def main():
    #Entrada
    angulo1 = pedir_int('\nDigite o valor do primeiro ângulo: ')
    angulo2 = pedir_int('Digite o valor do segundo ângulo: ')
    angulo3 = pedir_int('Digite o valor do terceiro ângulo: ')

    #Processamento
    tipo_triangulo = verificar_triangulo(angulo1, angulo2, angulo3)    

    #Saída
    mostrar_resultado(tipo_triangulo)

main()

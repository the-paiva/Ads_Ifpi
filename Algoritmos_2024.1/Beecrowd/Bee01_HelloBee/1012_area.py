#Pede mais de um valor em uma única linha
def pedir_multiplos_valores():
    return input().split()

#Calcula a área de um triângulo retângulo
def calcular_area_triangulo_retangulo(a, b):
    return (a * b) / 2

#Calcula a área de um círculo
def calcular_area_circulo(a):
    PI = 3.14159
    return PI * a**2

#Calcula a área de um trapézio
def calcular_area_trapezio(a, b, c):
    return ((a + b) * c) / 2

#Calcula a área de um quadrado
def calcular_area_quadrado(a):
    return a**2

#Calcula a área de um retângulo
def calcular_area_retangulo(a, b):
    return a * b

#Saída de dados do programa
def mostrar_resultado(area_triangulo_retangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo):
    print(f'TRIANGULO: {area_triangulo_retangulo:.3f}')
    print(f'CIRCULO: {area_circulo:.3f}')
    print(f'TRAPEZIO: {area_trapezio:.3f}')
    print(f'QUADRADO: {area_quadrado:.3f}')
    print(f'RETANGULO: {area_retangulo:.3f}')

def main():
    #Entrada
    a, b, c = pedir_multiplos_valores()

    #Processamento
    a, b, c = float(a), float(b), float(c)

    area_triangulo_retangulo = calcular_area_triangulo_retangulo(a, c)
    area_circulo = calcular_area_circulo(c)
    area_trapezio = calcular_area_trapezio(a, b, c)
    area_quadrado = calcular_area_quadrado(b)
    area_retangulo = calcular_area_retangulo(a, b)

    #Saída
    mostrar_resultado(area_triangulo_retangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo)

main()

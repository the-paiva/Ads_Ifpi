#Pede um número do tipo float
def pedir_float():
    return float(input())

#Calcula a área de um círculo
def calcular_area(raio):
    PI = 3.14159
    return PI * raio**2

#Saída de dados do programa
def mostrar_resultado(area):
    print(f'A={area:.4f}')

def main():
    #Entrada
    raio = pedir_float()

    #Processamento
    area = calcular_area(raio)

    #Saída
    mostrar_resultado(area)

main()

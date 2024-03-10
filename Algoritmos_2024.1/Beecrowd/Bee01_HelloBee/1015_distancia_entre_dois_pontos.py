#Pede mais de um valor em uma única linha
def pedir_multiplos_valores():
    return input().split()

#Converte variáveis para os seus tipos adequados (nesse caso, float)
def converter_tipos(x, y):
    return float(x), float(y)

#Calcula a distância entre dois pontos
def calcular_distancia(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Saída de dados do programa
def mostrar_resultado(distancia):
    print(f'{distancia:.4f}')

def main():
    #Entrada
    x1, y1 = pedir_multiplos_valores()
    x2, y2 = pedir_multiplos_valores()

    #Processamento
    x1, y1 = converter_tipos(x1, y1)
    x2, y2 = converter_tipos(x2, y2)

    distancia = calcular_distancia(x1, y1, x2, y2)

    #Saída
    mostrar_resultado(distancia)

main()

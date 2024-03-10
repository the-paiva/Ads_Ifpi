#Pede uma variável do tipo float
def pedir_float():
    return float(input())

#Calcula o volume de uma esfera
def calcular_volume(raio):
    PI = 3.14159
    return (4.0 / 3) * PI * raio**3

#Saída de dados do programa
def mostrar_resultado(volume):
    print(f'VOLUME = {volume:.3f}')

def main():
    #Entrada
    raio = pedir_float()

    #Processamento
    volume = calcular_volume(raio)

    #Saída
    mostrar_resultado(volume)

main()

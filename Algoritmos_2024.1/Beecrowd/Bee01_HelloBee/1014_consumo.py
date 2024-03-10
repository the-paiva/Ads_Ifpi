#Pede uma variável do tipo int
def pedir_int():
    return int(input())

#Pede uma variável do tipo float
def pedir_float():
    return float(input())

#Calcula o consumo médio de um automóvel
def calcular_consumo_medio(distancia_percorrida, combustivel_gasto):
    return distancia_percorrida / combustivel_gasto

#Saída de dados do programa
def mostrar_resultado(consumo_medio):
    print(f'{consumo_medio:.3f} km/l')

def main():
    #Entrada
    distancia_percorrida = pedir_int()
    combustivel_gasto = pedir_float()

    #Processamento
    consumo_medio = calcular_consumo_medio(distancia_percorrida, combustivel_gasto)

    #Saída
    mostrar_resultado(consumo_medio)

main()

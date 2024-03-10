#Pede uma variável do tipo int
def pedir_int():
    return int(input())

#Calcula a distância em minutos entre dois automóveis
def calcular_minutos(distancia):
    return distancia * 2

#Saída de dados do programa
def mostrar_resultado(minutos):
    print(f'{minutos} minutos')

def main():
    #Entrada
    distancia = pedir_int()

    #Processamento
    minutos = calcular_minutos(distancia)

    #Saída
    mostrar_resultado(minutos)

main()

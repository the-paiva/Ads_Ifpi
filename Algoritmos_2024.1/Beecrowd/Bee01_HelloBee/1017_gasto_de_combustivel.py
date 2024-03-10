#Pede uma variável do tipo int
def pedir_int():
    return int(input())

#Calcula a quantidade de litros necessária para a viagem
def calcular_quant_litros(tempo_gasto, velocidade_media):
    KML = 12
    return (tempo_gasto * velocidade_media) / KML

#Saída de dados do programa
def mostrar_resultado(quant_litros):
    print(f'{quant_litros:.3f}')

def main():
    #Entrada
    tempo_gasto = pedir_int()
    velocidade_media = pedir_int()

    #Processamento
    quant_litros = calcular_quant_litros(tempo_gasto, velocidade_media)

    #Saída
    mostrar_resultado(quant_litros)

main()

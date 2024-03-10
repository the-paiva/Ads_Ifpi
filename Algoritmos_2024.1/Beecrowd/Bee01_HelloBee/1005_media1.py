#Pede um número do tipo float
def pedir_float():
    return float(input())

#Calcula a média ponderada entre dois números
def calcular_media_ponderada(a, b):
    return (a * 3.5 + b * 7.5) / 11

#Saída de dados do programa
def mostrar_resultado(media):
    print(f'MEDIA = {media:.5f}')

def main():
    #Entrada
    a = pedir_float()
    b = pedir_float()

    #Processamento
    media = calcular_media_ponderada(a, b)

    #Saída
    mostrar_resultado(media)

main()

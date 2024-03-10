#Pede um número do tipo float
def pedir_float():
    return float(input())

#Calcula a média ponderada entre três números
def calcular_media_ponderada(a, b, c):
    return (a * 2 + b * 3 + c * 5) / 10

#Saída de dados do programa
def mostrar_resultado(media):
    print(f'MEDIA = {media:.1f}')

def main():
    #Entrada
    a = pedir_float()
    b = pedir_float()
    c = pedir_float()

    #Processamento
    media = calcular_media_ponderada(a, b, c)

    #Saída
    mostrar_resultado(media)

main()

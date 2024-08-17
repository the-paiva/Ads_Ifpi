#Calcule e escreva o valor de S.
#S = 1/1 + 3/2 + 5/3 + 7/4... 99/50

#Calcula o somatório de acordo com a sequência fornecida
def calcular_somatorio():
    somatorio = 0
    numerador = 1

    for denominador in range(1, 51):
        somatorio += numerador / denominador
        numerador += 2

    return somatorio

#Escreve o resultado do somatório
def mostrar_resultado(somatorio):
    print('\nSequência: S = 1/1 + 3/2 + 5/3 + 7/4... 99/50')
    print(f'Valor do somatório da sequência atual: {somatorio:.2f}')

def main():
    somatorio = calcular_somatorio()
    mostrar_resultado(somatorio)

main()

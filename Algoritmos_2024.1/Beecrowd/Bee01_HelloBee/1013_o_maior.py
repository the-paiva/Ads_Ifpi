#Pede mais de um valor em uma única linha
def pedir_multiplos_valores():
    return input().split()

#Retorna o maior entre dois números
def calcular_maior_num(a, b):
    return (a + b + abs(a - b)) / 2

#Saída de dados do programa
def mostrar_resultado(maior):
    print(f'{maior:.0f} eh o maior')

def main():
    #Entrada
    a, b, c = pedir_multiplos_valores()

    #Processamento
    a, b, c = int(a), int(b), int(c)

    maior = calcular_maior_num(a, b)
    maior = calcular_maior_num(maior, c)

    #Saída
    mostrar_resultado(maior)

main()

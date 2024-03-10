#Pede um número do tipo int
def pedir_int():
    return int(input())

#Calcula a diferença entre os produtos
def calcular_diferenca(a, b, c, d):
    return a * b - c * d

#Saída de dados do programa
def mostrar_resultado(diff):
    print(f'DIFERENCA = {diff}')

def main():
    #Entrada
    a = pedir_int()
    b = pedir_int()
    c = pedir_int()
    d = pedir_int()

    #Processamento
    diff = calcular_diferenca(a, b, c, d)

    #Saída
    mostrar_resultado(diff)

main()

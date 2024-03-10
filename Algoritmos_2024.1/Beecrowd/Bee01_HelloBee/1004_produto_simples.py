#Pede um número do tipo int
def pedir_int():
    num = int(input())
    return num

#Realiza a multiplicação entre dois números inteiros
def multiplicar_inteiros(a, b):
    return a * b

def main():
    #Entrada
    a = pedir_int()
    b = pedir_int()

    #Processamento
    prod = multiplicar_inteiros(a, b)

    #Saída
    print(f'PROD = {prod}')

main()

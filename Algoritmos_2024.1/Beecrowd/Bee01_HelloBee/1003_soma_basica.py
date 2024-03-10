#Pede um número do tipo int
def pedir_int():
    num = int(input())
    return num

#Realiza a soma entre dois números inteiros
def somar_inteiros(a, b):
    return a + b

def main():
    #Entrada
    a = pedir_int()
    b = pedir_int()

    #Processamento
    soma = somar_inteiros(a, b)

    #Saída
    print(f'SOMA = {soma}')

main()

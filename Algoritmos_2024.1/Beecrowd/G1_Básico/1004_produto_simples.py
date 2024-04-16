#Pede um número do tipo int
def pedir_int():
    num = int(input())
    return num

#Realiza a multiplicação entre dois números inteiros
def multiplicar_inteiros(a, b):
    return a * b

def main():
    a = pedir_int()
    b = pedir_int()
    prod = multiplicar_inteiros(a, b)
    
    print(f'PROD = {prod}')

main()

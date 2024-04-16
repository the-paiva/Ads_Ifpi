#Pede um número do tipo int
def pedir_int():
    num = int(input())
    return num

#Realiza a soma entre dois números inteiros
def somar_inteiros(a, b):
    return a + b

def main():
    a = pedir_int()
    b = pedir_int()
    soma = somar_inteiros(a, b)

    print(f'SOMA = {soma}')

main()

#Leia 1 (um) número inteiro e escreva se este número é par ou impar.

#Pede uma variável do tipo int
def pedir_int(texto):
    return int(input(texto))

#Verifica se um número é par ou ímpar
def verificar_par(num):
    if num % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'
    
#Saída de dados do programa
def mostrar_resultado(num, tipo_num):
    print(f'{num} é um número {tipo_num}.')

def main():
    num = pedir_int('\nDigite um número inteiro: ')
    tipo_num = verificar_par(num)
    mostrar_resultado(num, tipo_num)

main()

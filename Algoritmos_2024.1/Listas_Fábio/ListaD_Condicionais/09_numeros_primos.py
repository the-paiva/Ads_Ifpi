#Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

#Pede um número do tipo int
def pedir_int(texto):
    num = int(input(texto))
    return num

#Verifica se um número é divísivel por 2 (com excessão do próprio 2)
def eh_divisivel_por_2(num):
    if num != 2 and num % 2 == 0:
        return True
    else:
        return False

#Verifica se um número é divísivel por 3 (com excessão do próprio 3)
def eh_divisivel_por_3(num):
    dezena = num // 10
    unidade = num % 10

    if num != 3 and (dezena + unidade) % 3 == 0:
        return True
    else:
        return False

#Verifica se um número é divisível por 5 (com excessão do próprio 5)
def eh_divisivel_por_5(num):
    unidade = num % 10

    if num != 5 and unidade % 5 == 0:
        return True
    else:
        return False

#Verifica se um número é divisível por 7 (com excessão do próprio 7)
def eh_divisivel_por_7(num):
    if num != 7 and num % 7 == 0:
        return True
    else:
        return False

#Verifica se um número é primo de acordo com sua divisibilidade
def verificar_divisibilidades(num):
    divisivel_por_2 = eh_divisivel_por_2(num)
    divisivel_por_3 = eh_divisivel_por_3(num)
    divisivel_por_5 = eh_divisivel_por_5(num)
    divisivel_por_7 = eh_divisivel_por_7(num)

    if (divisivel_por_2 or divisivel_por_3 or divisivel_por_5 or divisivel_por_7):
        return 'COMPOSTO (NÃO PRIMO)'
    else:
        return 'PRIMO'

#Saída de dados do programa
def mostrar_resultado(num, tipo):
    if num >= 0 and num <= 100:
        print(f'\n{num} é um número {tipo}.')
    else:
        print('\nNÚMERO INVÁLIDO!')

def main():
    #Entrada
    num = pedir_int('\nDigite um número de 0 até 100: ')

    #Processamento
    tipo = verificar_divisibilidades(num)

    #Saída
    mostrar_resultado(num, tipo)

main()

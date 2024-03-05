#Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é 
#igual ou diferente do algarismo da unidade.

#Pede um número do tipo int
def pedir_int(texto):
    num = int(input(texto))
    return num

#Separa a unidade e a dezena de um número
def separar_numero(num):
    dezena = num // 10
    unidade = num % 10
    return dezena, unidade

#Verifica se dois números são iguais
def eh_igual(dezena, unidade):
    if dezena == unidade:
        return 'iguais'
    else:
        return 'diferentes'
    
#Saída de dados do programa
def mostrar_resultado(num, situacao):
    print(f'\nOs algarismos de {num} são {situacao} entre si!')

def main():
    #Entrada
    num = pedir_int('\nDigite um número inteiro de dois dígitos: ')

    #Processamento
    dezena, unidade = separar_numero(num)
    situacao = eh_igual(dezena, unidade)

    #Saída
    mostrar_resultado(num, situacao)

main()

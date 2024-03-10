#Pede mais de um valor em uma única linha
def pedir_multiplos_valores():
    return input().split()

#Converte os dados de entrada para seus tipos apropriados
def converter_tipos(cod_peca, num_peca, valor_peca):
    return int(cod_peca), int(num_peca), float(valor_peca)

#Calcula o valor total de um número de peças
def calcular_valor_total(num_peca, valor_peca):
    return num_peca * valor_peca

#Saída de dados do programa
def mostrar_resultado(valor_total):
    print(f'VALOR A PAGAR: R$ {valor_total:.2f}')

def main():
    #Entrada
    cod_peca1, num_peca1, valor_peca1 = pedir_multiplos_valores()
    cod_peca2, num_peca2, valor_peca2 = pedir_multiplos_valores()

    #Processamento
    cod_peca1, num_peca1, valor_peca1 = converter_tipos(cod_peca1, num_peca1, valor_peca1)
    cod_peca2, num_peca2, valor_peca2 = converter_tipos(cod_peca2, num_peca2, valor_peca2)

    valor_total = calcular_valor_total(num_peca1, valor_peca1)
    valor_total += calcular_valor_total(num_peca2, valor_peca2)

    #Saída
    mostrar_resultado(valor_total)

main()

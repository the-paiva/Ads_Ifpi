#Pede uma variável do tipo string
def pedir_string():
    return str(input())

#Pede uma variável do tipo inteiro
def pedir_float():
    return float(input())

#Calcula o salário total de um vendedor (salário fixo + comissão)
def calcular_salario_total(salario_fixo, montante_vendas):
    return salario_fixo + (montante_vendas * 15 / 100)

#Saída de dados do programa
def mostrar_resultado(salario_total):
    print(f'TOTAL = R$ {salario_total:.2f}')

def main():
    #Entrada
    nome = pedir_string()
    salario_fixo = pedir_float()
    montante_vendas = pedir_float()

    #Processamento
    salario_total = calcular_salario_total(salario_fixo, montante_vendas)

    #Saída
    mostrar_resultado(salario_total)

main()

#Pede um número do tipo int
def pedir_int():
    return int(input())

#Pede um número do tipo float
def pedir_float():
    return float(input())

#Calcula o salário de um funcionário
def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

#Saída de dados do programa
def mostrar_resultado(num_funcionario, salario):
    print(f'NUMBER = {num_funcionario}\nSALARY = U$ {salario:.2f}')

def main():
    #Entrada
    num_funcionario = pedir_int()
    horas_trabalhadas = pedir_int()
    valor_hora = pedir_float()

    #Processamento
    salario = calcular_salario(horas_trabalhadas, valor_hora)

    #Saída
    mostrar_resultado(num_funcionario, salario)

main()

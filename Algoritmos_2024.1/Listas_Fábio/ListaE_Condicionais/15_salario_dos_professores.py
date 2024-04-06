#Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

#Pede uma variável do tipo string
def pedir_string(texto):
    return str(input(texto))

#Pede uma variável do tipo int
def pedir_int(texto):
    return int(input(texto))

#Pede uma variável do tipo float
def pedir_float(texto):
    return float(input(texto))

#Verifica se dois valores são iguais
def eh_igual(a, b):
    if a == b:
        return True
    else:
        return False

#Faz uma multiplicação
def multiplicar(a, b):
    return a * b

#Verifica qual professor tem o mesmo salário
def checar_prof_com_maior_salario(prof1, prof2, salario_prof1, salario_prof2):
    if salario_prof1 > salario_prof2:
        return prof1
    else:
        return prof2

#Mostra o salário dos dois professores
def mostrar_salarios(prof1, prof2, salario_prof1, salario_prof2):
    print(f'\n{prof1}: R$ {salario_prof1:.2f}')
    print(f'{prof2}: R$ {salario_prof2:.2f}')

#Saída de dados do programa com salários diferentes
def mostrar_resultado_diferentes(maior_prof):
    print(f'\nO maior salário é de {maior_prof}')

#Saída de dados do programa com salários iguais
def mostrar_resultado_iguais():
    print('\nOs dois salários são iguais!')

def main():
    prof1 = pedir_string('\nDigite o nome do primeiro professor: ')
    horas_prof1 = pedir_int(f'Digite a quantidade de horas de aula de {prof1}: ')
    valor_hora_prof1 = pedir_float(f'Digite o valor por hora recebido por {prof1}: R$ ')

    prof2 = pedir_string('\nDigite o nome do primeiro professor: ')
    horas_prof2 = pedir_int(f'Digite a quantidade de horas de aula de {prof2}: ')
    valor_hora_prof2 = pedir_float(f'Digite o valor por hora recebido por {prof2}: R$ ')

    salario_prof1 = multiplicar(horas_prof1, valor_hora_prof1)
    salario_prof2 = multiplicar(horas_prof2, valor_hora_prof2)

    igual = eh_igual(salario_prof1, salario_prof2)

    if not igual:
        maior_prof = checar_prof_com_maior_salario(prof1, prof2, salario_prof1, salario_prof2)
        
        mostrar_salarios(prof1, prof2, salario_prof1, salario_prof2)
        mostrar_resultado_diferentes(maior_prof)
    else:
        mostrar_salarios(prof1, prof2, salario_prof1, salario_prof2)
        mostrar_resultado_iguais()

main()

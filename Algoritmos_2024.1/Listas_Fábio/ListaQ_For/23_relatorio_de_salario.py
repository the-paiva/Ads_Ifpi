#Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
#horas trabalhadas e o seu número de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
#40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
#Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
#funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
#líquido do funcionário.

from Utils.io_utils import pedir_int_min, pedir_float_min

#Obtém os dados necessários de um funcionário para o relatório de salário
def obter_dados_do_funcionario(cont):
    print('\n=====================================================================')
    print(f'Funcionário {cont + 1}:')
    codigo_funcionario = pedir_int_min('-> Digite o código do funcionário: ', 1)
    horas_trabalhadas = pedir_float_min('-> Digite o número de horas trabalhadas: ', 1)
    quant_dependentes = pedir_int_min('-> Digite o número de dependentes: ', 0)

    return codigo_funcionario, horas_trabalhadas, quant_dependentes

#Calcula o salário bruto de um funcionário
def calcular_salario_bruto(horas_trabalhadas, quant_dependentes):
    SALARIO_POR_HORA = 12
    SALARIO_POR_DEPENDENTE = 40
    salario_bruto = (horas_trabalhadas * SALARIO_POR_HORA) + (quant_dependentes * SALARIO_POR_DEPENDENTE)

    return salario_bruto

#Calcula os descontos de INSS e IR de um funcionário
def calcular_descontos(salario_bruto):
    desconto_inss = salario_bruto * 0.085
    desconto_ir = salario_bruto * 0.05
    
    return desconto_inss, desconto_ir

#Calcula o salário líquido de um funcionário
def calcular_salario_liquido(salario_bruto, desconto_inss, desconto_ir):
    salario_liquido = salario_bruto - (desconto_inss + desconto_ir)
    return salario_liquido

#Escreve o relatório do salário de um funcionário
def escrever_relatorio(cont, codigo_funcionario, desconto_inss, desconto_ir, salario_liquido):
    print(f'\nRelatório do funcionário {cont + 1}')
    print(f'- Código do uncionário: {codigo_funcionario}')
    print(f'- Desconto INSS: R$ {desconto_inss:.2f}')
    print(f'- Desconto IR: R$ {desconto_ir:.2f}')
    print(f'- Salário Líquido: R$ {salario_liquido:.2f}')

def main():
    quant_funcionarios = pedir_int_min('Digite a quantidade de funcionários: ', 1)

    for cont in range(quant_funcionarios):
        codigo_funcionario, horas_trabalhadas, quant_dependentes = obter_dados_do_funcionario(cont)
        
        salario_bruto = calcular_salario_bruto(horas_trabalhadas, quant_dependentes)
        desconto_inss, desconto_ir = calcular_descontos(salario_bruto)
        salario_liquido = calcular_salario_liquido(salario_bruto, desconto_inss, desconto_ir)
        
        escrever_relatorio(cont, codigo_funcionario, desconto_inss, desconto_ir, salario_liquido)

main()

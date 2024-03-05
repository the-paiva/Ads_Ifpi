#Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule 
#e escreva sua idade exata (em anos).

#Pede um número do tipo int
def pedir_int(texto):
    num = int(input(texto))
    return num

#Verifica se um ano é bissexto
def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

#Verifica se uma data é válida
def verificar_data(dia, mes, ano, eh_bissexto):
    if ano < 1:
        return False
    
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: #Meses com 31 dias
        if dia >= 1 and dia <= 31:
            return True
        else:
            return False
    elif mes==4 or mes==6 or mes==9 or mes==11: #Meses com 30 dias
        if dia >= 1 and dia <= 30:
            return True
        else:
            return False
    elif mes == 2: #Fevereiro
        if dia >= 1 and ((eh_bissexto and dia <= 29) or (eh_bissexto == False and dia <= 28)):
            return True
        else:
            return False
    else:
        return False

#Calcula a idade de uma pessoa conforme as datas digitadas
def calcular_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    if (mes_atual < mes_nasc) or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        return (ano_atual - ano_nasc) - 1
    return ano_atual - ano_nasc

#Verifica se a idade calculada é válida (Evitando idades menores do que 1)
def eh_idade_valida(idade):
    if idade >= 1:
        return True
    else:
        return False

#Saída de dados do programa
def mostrar_resultado(tipo_data_atual, tipo_data_nasc, idade, idade_valida):
    if tipo_data_atual and tipo_data_nasc and idade_valida:
        print(f'\nAs datas digitadas são válidas\nVocê tem {idade} anos.')
    else:
        print('\nUma ou mais datas digitadas são inválidas.')

def main():
    #Entrada
    dia_atual = pedir_int('\nDigite o dia atual: ')
    mes_atual = pedir_int('Digite o mês atual: ')
    ano_atual = pedir_int('Digite o ano total: ')

    dia_nasc = pedir_int('\nDigite o seu dia de nascimento: ')
    mes_nasc = pedir_int('Digite o seu mês de nascimento: ')
    ano_nasc = pedir_int('Digite o seu ano de nascimento: ')

    #Processamento
    eh_bissexto_atual = verificar_ano_bissexto(ano_atual)
    eh_bissexto_nasc = verificar_ano_bissexto(ano_nasc)
    tipo_data_atual = verificar_data(dia_atual, mes_atual, ano_atual, eh_bissexto_atual)
    tipo_data_nasc = verificar_data(dia_nasc, mes_nasc, ano_nasc, eh_bissexto_nasc)

    idade = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    idade_valida = eh_idade_valida(idade)

    #Saída
    mostrar_resultado(tipo_data_atual, tipo_data_nasc, idade, idade_valida)

main()

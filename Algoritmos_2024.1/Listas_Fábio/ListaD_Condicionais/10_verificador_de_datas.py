#Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

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
        return 'INVÁLIDA'
    
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: #Meses com 31 dias
        if dia >= 1 and dia <= 31:
            return 'VÁLIDA'
        else:
            return 'INVÁLIDA'
    elif mes==4 or mes==6 or mes==9 or mes==11: #Meses com 30 dias
        if dia >= 1 and dia <= 30:
            return 'VÁLIDA'
        else:
            return 'INVÁLIDA'
    elif mes == 2: #Fevereiro
        if dia >= 1 and ((eh_bissexto and dia <= 29) or (eh_bissexto == False and dia <= 28)):
            return 'VÁLIDA'
        else:
            return 'INVÁLIDA'
    else:
        return 'INVÁLIDA'

#Saída de dados do programa
def mostrar_resultado(tipo_data):
    print(f'\nA data digitada é {tipo_data}.')

def main():
    #Entrada
    dia = pedir_int('\nDigite um dia: ')
    mes = pedir_int('Digite um mês: ')
    ano = pedir_int('Digite um ano: ')

    #Processamento
    eh_bissexto = verificar_ano_bissexto(ano)
    tipo_data = verificar_data(dia, mes, ano, eh_bissexto)

    #Saída
    mostrar_resultado(tipo_data)

main()

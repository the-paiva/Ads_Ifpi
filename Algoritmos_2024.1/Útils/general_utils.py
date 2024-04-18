#Verifica se um ano é bissexto
#(Um ano é bissexto se for divisível por 4, exceto quando também é divisível por 100, a menos 
#que seja divisível por 400)
def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

#Verifica se uma data digitada é válida
def eh_data_valida(dia, mes, ano):
    if dia > 31 or mes > 12 or mes < 1:
        return False
    elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return False
    elif mes == 2 and dia > 29:
        return False
    elif mes == 2 and dia > 28 and ano % 4 != 0:
        return False
    
    return True

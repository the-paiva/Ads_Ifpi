#Pede um valor int
def pedir_int(texto):
    return int(input(texto))

#Pede um valor int com um limite mínimo
def pedir_int_min(texto, min):
    num = int(input(texto))

    if num < min:
        num = pedir_int_min(texto, min)

    return num

#Pede um valor int com um limite máximo
def pedir_int_max(texto, max):
    num = int(input(texto))

    if num > max:
        num = pedir_int_max(texto, max)

    return num

#Pede um valor int com limite mínimo e limite máximo
def pedir_int_min_max(texto, min, max):
    num = int(input(texto))

    if num < min or num > max:
        num = pedir_int_min_max(texto, min, max)

    return num

#Pede um valor float
def pedir_float(texto):
    return float(input(texto))

#Pede um valor float com um limite mínimo
def pedir_float_min(texto, min):
    num = float(input(texto))

    if num < min:
        num = pedir_float_min(texto, min)

    return num

#Pede um valor float com um limite máximo
def pedir_float_max(texto, max):
    num = float(input(texto))

    if num > max:
        num = pedir_float_max(texto, max)

    return num

#Pede um valor float com limite mínimo e máximo
def pedir_float_min_max(texto, min, max):
    num = float(input(texto))

    if num < min or num > max:
        num = pedir_float_min_max(texto, min, max)

    return num

#Pede um valor string
def pedir_string(texto):
    return str(input(texto))

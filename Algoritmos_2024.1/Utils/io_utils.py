#Arquivo que reúne as funções padrões referentes a operações de entrada e saída de dados


#Pede um valor int
pedir_int = lambda texto: int(input(texto))


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


#Pede um valor int que não aceita como entrada um número específico
def pedir_int_restrito(texto, valor_proibido):
    num = int(input(texto))

    if num == valor_proibido:
        num = pedir_int_restrito(texto, valor_proibido)

    return num


#Pede um valor float
pedir_float = lambda texto: float(input(texto))


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


#Pede um valor float que não aceita como entrada um número específico
def pedir_float_restrito(texto, valor_proibido):
    num = float(input(texto))

    if num == valor_proibido:
        num = pedir_float_restrito(texto, valor_proibido)

    return num


#Pede um valor string
pedir_string = lambda texto: str(input(texto))

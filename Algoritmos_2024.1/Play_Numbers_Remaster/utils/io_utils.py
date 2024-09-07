#Arquivo que reúne as funções padrões referentes a operações de entrada e saída de dados


#Pede um valor int
pedir_int = lambda texto: int(input(texto))


#Pede um valor int com um limite mínimo
def pedir_int_min(texto, num_min):
    num = int(input(texto))
    return (lambda: pedir_int_min(texto, num_min))() if num < num_min else num


#Pede um valor int com um limite máximo
def pedir_int_max(texto, num_max):
    num = int(input(texto))
    return (lambda: pedir_int_max(texto, num_max))() if num > num_max else num


#Pede um valor int com limite mínimo e limite máximo
def pedir_int_min_max(texto, num_min, num_max):
    num = int(input(texto))
    return (lambda: pedir_int_min_max(texto, num_min, num_max))() if num < num_min or num > num_max else num


#Pede um valor int que não aceita como entrada um número específico
def pedir_int_restrito(texto, valor_proibido):
    num = int(input(texto))
    return (lambda: pedir_int_restrito(texto, valor_proibido))() if num == valor_proibido else num


#Pede um valor float
pedir_float = lambda texto: float(input(texto))


#Pede um valor float com um limite mínimo
def pedir_float_min(texto, num_min):
    num = float(input(texto))
    return (lambda: pedir_float_min(texto, num_min))() if num < num_min else num


#Pede um valor float com um limite máximo
def pedir_float_max(texto, num_max):
    num = float(input(texto))
    return (lambda: pedir_float_max(texto, num_max))() if num > num_max else num


#Pede um valor float com limite mínimo e máximo
def pedir_float_min_max(texto, num_min, num_max):
    num = float(input(texto))
    return (lambda: pedir_float_min_max(texto, num_min, num_max))() if num < num_min or num > num_max else num


#Pede um valor float que não aceita como entrada um número específico
def pedir_float_restrito(texto, valor_proibido):
    num = float(input(texto))
    return (lambda: pedir_float_restrito(texto, valor_proibido))() if num == valor_proibido else num


#Pede um valor string
pedir_string = lambda texto: str(input(texto))

#Arquivo que reúne as funções padrões referentes a operações matemáticas


#Verifica se dois números são iguais
eh_igual = lambda num1, num2: True if num1 == num2 else False


#Verifica se um número é maior do que o outro
eh_maior = lambda num, num_de_comparacao: True if num > num_de_comparacao else False


#Verifica se um número é menor do que o outro
eh_menor = lambda num, num_de_comparacao: True if num < num_de_comparacao else False


#Verifica se um número é par
eh_par = lambda num: True if num % 2 == 0 else False


#Verifica se um número é ímpar
eh_impar = lambda num: True if num % 2 != 0 else False


#Verifica se um número é primo (Válido apenas para números entre 0 e 100)
def eh_primo(num):
    dezena = num // 10
    unidade = num % 10

    if ((num != 2 and num % 2 == 0) or (num != 3 and (dezena + unidade) % 3 == 0) or 
    (num != 5 and unidade % 5 == 0) or (num != 7 and num % 7 == 0)):
        return False
    
    return True


#Retorna o maior entre dois números (Ignorando casos de números iguais)
def checar_maior(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


#Retorna o menor entre dois números (Ignorando casos de números iguais)
def checar_menor(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


#Separa números com duas casas decimais
def dividir_dezena(num):
    dezena = num // 10
    unidade = num % 10

    return dezena, unidade


#Separa números com três casas decimais
def dividir_centena(num):
    centena = num // 100
    resto = num % 100
    dezena, unidade = dividir_dezena(resto)

    return centena, dezena, unidade


#Separa números com quatro casas decimais
def dividir_milhar(num):
    milhar = num // 1000
    resto = num % 1000
    centena, dezena, unidade = dividir_centena(resto)
    
    return milhar, centena, dezena, unidade


#Calcula a média aritmética
calcular_media_aritmetica = lambda somatorio, quant_elementos: somatorio / quant_elementos if quant_elementos > 0 else 0


#Verifica se os lados digitados formam um triângulo
eh_triangulo = lambda maior_lado, lado_menor1, lado_menor2: True if lado_menor1 + lado_menor2 > maior_lado else False


#Verifica se um valor é positivo
eh_positivo = lambda num: True if num > 0 else False

    
#Verifica se um valor é negativo
eh_negativo = lambda num: True if num < 0 else False


#Verifica se um valor é nulo (0)
eh_nulo = lambda num: True if num == 0 else False


#Calcula o módulo de um número
calcular_modulo = lambda num: num if num >= 0 else num * (-1)


#Calcula o delta para uma equação do segundo grau
calcular_delta = lambda a, b, c: b**2 - 4 * a * c


#Calcula as raízes de uma equação do segundo grau
def formula_de_bhaskara(a, b, delta):
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)

    return x1, x2


#Calcula a raíz quadrada de um número
calcular_raiz_quadrada = lambda num: num**0.5


#Arrendonda um número para cima (caso a parte fracionária seja maior do que 0.5) ou
#para baixo (caso a parte fracionária seja menor do que 0.5)
def arredondar_numero(num):
    if num >= 0:
        parte_inteira = int(num)
        parte_fracionaria = num - parte_inteira
    else:
        parte_inteira = int(-num)
        parte_fracionaria = -num - parte_inteira

    if parte_fracionaria >= 0.5:
        return parte_inteira + 1
    else:
        return parte_inteira


#Realiza um cálculo de porcentagem
calcular_porcentagem = lambda valor_base, percentual: valor_base * percentual / 100


#Verifica se um número é inteiro
eh_inteiro = lambda num: True if num - int(num) == 0 else False


#Verifica se um número é decimal
eh_decimal = lambda num: True if num - int(num) != 0 else False


#Verifica se um número é múltiplo de outro
eh_multiplo = lambda num1, num2: True if num1 % num2 == 0 else False


#Formata um número para uma quantidade específica de casas decimais
truncar_casas_decimais = lambda num, casas_decimais: int(num * 10**casas_decimais) / 10**casas_decimais

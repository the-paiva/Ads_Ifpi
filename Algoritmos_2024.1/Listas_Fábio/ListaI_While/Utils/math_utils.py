#Verifica se dois números são iguais
def eh_igual(num1, num2):
    if num1 == num2:
        return True

    return False

#Verifica se um número é maior do que o outro
def eh_maior(num1, num2):
    if num1 > num2:
        return True
    
    return False

#Verifica se um número é menor do que o outro
def eh_menor(num1, num2):
    if num1 < num2:
        return True
    
    return False

#Verifica se um número é par
def eh_par(num):
    if num % 2 == 0:
        return True
    
    return False

#Verifica se um número é ímpar
def eh_impar(num):
    if num % 2 != 0:
        return True
    
    return False

#Verifica se um número é primo (Válido apenas para números entre 0 e 100)
def eh_primo(num):
    dezena = num // 10
    unidade = num % 10

    if ((num != 2 and num % 2 == 0) or (num != 3 and (dezena + unidade) % 3 == 0) or 
    (num != 5 and unidade % 5 == 0) or (num != 7 and num % 7 == 0)):
        return True
    
    return False

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
def calcular_media_aritmetica(somatorio, quant_elementos):
    return somatorio / quant_elementos

#Verifica se os lados digitados formam um triângulo
def eh_triangulo(maior_lado, lado_menor1, lado_menor2):
    if lado_menor1 + lado_menor2 > maior_lado:
        return True
    
    return False

#Verifica se um valor é positivo
def eh_positivo(num):
    if num > 0:
        return True
    
    return False
    
#Verifica se um valor é negativo
def eh_negativo(num):
    if num < 0:
        return True
    
    return False

#Verifica se um valor é nulo (0)
def eh_nulo(num):
    if num == 0:
        return True
    
    return False

#Calcula o módulo de um número
def calcular_modulo(num):
    if num >= 0:
        return num
    
    return num * (-1)

#Calcula o delta para uma equação do segundo grau
def calcular_delta(a, b, c):
    return b**2 - 4 * a * c

#Calcula as raízes de uma equação do segundo grau
def formula_de_bhaskara(a, b, delta):
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)

    return x1, x2

#Calcula a raíz quadrada de um número
def calcular_raiz_quadrada(num):
    return num**0.5

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
def calcular_porcentagem(valor_base, percentual):
    return valor_base * percentual / 100

#Verifica se um número é inteiro
def eh_inteiro(num):
    if num - int(num) == 0:
        return True
    
    return False

#Verifica se um número é decimal
def eh_decimal(num):
    if num - int(num) != 0:
        return True
    
    return False

#Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes.
#Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).

from Utils.io_utils import pedir_float
from Utils.math_utils import eh_positivo

#Pede um valor float que não aceita como entrada um número específico
def pedir_float_restrito(texto, valor_proibido):
    num = float(input(texto))

    if num == valor_proibido:
        num = pedir_float_restrito(texto, valor_proibido)

    return num

#Calcula o delta para uma equação do segundo grau
def calcular_delta(a, b, c):
    return b**2 - 4 * a * c

#Calcula as raízes de uma equação do segundo grau
def formula_de_bhaskara(a, b, delta):
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)

    return x1, x2

#Escreve na tela os resultados de uma equação com raízes reais
def mostrar_resultado_com_raizes_reais(x1, x2, delta):
    print(f"""\n========== RAÍZES ==========
    DELTA: {delta:.2f}
    X1 = {x1:.2f}
    X2 = {x2:.2f}""")

#Escreve na tela os resultados de uma equação sem raízes reais
def mostrar_resultado_sem_raizes_reais(delta):
    print(f'\nO discriminante dessa equação é negativo ({delta:.2f}).')
    print('Portanto, ela não tem raízes reais.')

def main():
    a = pedir_float_restrito('\nDigite o valor do coeficiente a (Não pode ser 0): ', 0)
    b = pedir_float('Digite o valor do coeficiente b: ')
    c = pedir_float('Digite o valor do coeficiente c: ')

    delta = calcular_delta(a, b, c)
    x1, x2 = formula_de_bhaskara(a, b, delta)

    if eh_positivo(delta):
        mostrar_resultado_com_raizes_reais(x1, x2, delta)
    else:
        mostrar_resultado_sem_raizes_reais(delta)

main()

#Escreva um algoritmo que gere um número aleatório inteiro (utilize a função rand(): aleatorio = rand())
#e solicite um número ao usuário. O objetivo é que o usuário acerte o número gerado. Se o número
#digitado for menor que o gerado, escreva “Maior”, se for maior, escreva “Menor”, e solicite novamente
#um número ao usuário. Repita este processo ate que o usuário acerte o número gerado. Após isso,
#escreva em quantas tentativas o usuário acertou.

from Utils.io_utils import pedir_int_min_max
from random import randint

#Verifica se o usuário acertou o número gerado
def acerto(numero_digitado, numero_gerado):
    if numero_digitado == numero_gerado:
        return True
    
    return False

#Analisa se o número digitado é maior ou menor que o número gerado, atribuindo uma dica a uma string
def atribuir_dica(numero_digitado, numero_gerado):
    if numero_digitado < numero_gerado:
        return 'Maior'
    elif numero_digitado > numero_gerado:
        return 'Menor'

    return ''

def main():
    numero_gerado = randint(1, 100)
    numero_digitado = -1
    tentativas = 0
    
    while not acerto(numero_digitado, numero_gerado):
        numero_digitado = pedir_int_min_max('Digite um número inteiro entre 1 e 100: ', 1, 100)
        tentativas += 1
        
        dica = atribuir_dica(numero_digitado, numero_gerado)
        print(dica)
    
    print(f'Você acertou o número em {tentativas} tentativas.')

main()

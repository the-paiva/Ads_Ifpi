#Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria 
#for maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
#contrario, é arredondado para o inteiro imediatamente inferior.

from Utils.io_utils import pedir_float

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

#Escreve o resultado do arredondamento
def escrever_resultado(num, num_arredondado):
    print(f'\nNúmero digitado: {num}')
    print(f'Número arredondado: {num_arredondado}')

def main():
    num = pedir_float('\nDigite um número para o arredondamento: ')
    num_arredondado = arredondar_numero(num)
    escrever_resultado(num, num_arredondado)

main()

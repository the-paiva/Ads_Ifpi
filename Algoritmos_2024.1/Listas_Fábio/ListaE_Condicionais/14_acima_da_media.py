#Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

#Pede um valor int
def pedir_int(texto):
    return int(input(texto))

#Calcula a média aritmética dos cinco números digitados
def calcular_media(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5

#Verifica se um número é maior que o outro
def eh_maior(num1, num2):
    if num1 > num2:
        return True
    
    return False

#Escreve a média calculada
def escrever_media(media):
    print('')
    print('-' * 50)
    print(f'Média: {media:.2f}')

#Escreve os números que são maiores do que a média
def escrever_numeros_acima_da_media(num1, num2, num3, num4, num5, media):
    print('\nNúmeros maiores que a média: ')

    if eh_maior(num1, media):
        print(num1)
    if eh_maior(num2, media):
        print(num2)
    if eh_maior(num3, media):
        print(num3)
    if eh_maior(num4, media):
        print(num4)
    if eh_maior(num5, media):
        print(num5)

    print('-' * 50)

def main():
    num1 = pedir_int('\nDigite o primeiro número: ')
    num2 = pedir_int('Digite o segundo número: ')
    num3 = pedir_int('Digite o terceiro número: ')
    num4 = pedir_int('Digite o quarto número: ')
    num5 = pedir_int('Digite o quinto número: ')
    
    media = calcular_media(num1, num2, num3, num4, num5)
    escrever_media(media)
    escrever_numeros_acima_da_media(num1, num2, num3, num4, num5, media)

main()

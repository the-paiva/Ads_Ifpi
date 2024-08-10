#Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.o de identificação e seu
#peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.o de identificação e o peso do
#boi mais magro e do boi mais gordo. (Flag: n.o identificação=0)

from Utils.io_utils import pedir_int_min, pedir_float_min_max

#Verifica se o boi atual é o mais magro e retorna nome e peso
def verificar_boi_mais_magro(identificacao, peso, boi_mais_magro, menor_peso):
    if peso < menor_peso:
        return identificacao, peso
    
    return boi_mais_magro, menor_peso

#Verifica se o boi atual é o mais gordo e retorna nome e peso
def verificar_boi_mais_gordo(identificacao, peso, boi_mais_gordo, maior_peso):
    if peso > maior_peso:
        return identificacao, peso
    
    return boi_mais_gordo, maior_peso

#Mostra o resultado do peso dos bois
def mostrar_resultados(boi_mais_magro, menor_peso, boi_mais_gordo, maior_peso):
    print('\n================ RESULTADOS ================')
    print(f'Número de identificação do boi mais magro: {boi_mais_magro}')
    print(f'Peso do boi mais magro: {menor_peso:.2f} Kg')
    print(f'\nNúmero de identificação do boi mais gordo: {boi_mais_gordo}')
    print(f'Peso do boi mais gordo: {maior_peso:.2f} Kg')

def main():
    identificacao = -1
    count = 0
    menor_peso = 9999
    maior_peso = 0
    boi_mais_magro, boi_mais_gordo = 0, 0

    while identificacao != 0:
        print(f'\nCartão {count + 1}')
        identificacao = pedir_int_min('Digite o número de identificação do boi: ', 0)

        if identificacao != 0:
            peso = pedir_float_min_max('Digite o peso do boi (em kg): ', 250, 1000)

            boi_mais_magro, menor_peso = verificar_boi_mais_magro(identificacao, peso, boi_mais_magro, menor_peso)
            boi_mais_gordo, maior_peso = verificar_boi_mais_gordo(identificacao, peso, boi_mais_gordo, maior_peso)

            count += 1

    if count >= 1:
        mostrar_resultados(boi_mais_magro, menor_peso, boi_mais_gordo, maior_peso)
    else:
        print('\nNenhum boi foi registrado!')

main()

#Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
#nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
#numero de identificação e o peso do boi mais magro e do boi mais gordo.

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
    menor_peso = 9999
    maior_peso = 0
    boi_mais_magro, boi_mais_gordo = 0, 0

    quant_fichas = pedir_int_min('Digite quantas fichas serão registradas: ', 1)

    for cont in range(quant_fichas):
        print(f'\nFicha {cont + 1}')
        identificacao = pedir_int_min('Digite o número de identificação do boi: ', 0)

        peso = pedir_float_min_max('Digite o peso do boi (em kg): ', 250, 1000)

        boi_mais_magro, menor_peso = verificar_boi_mais_magro(identificacao, peso, boi_mais_magro, menor_peso)
        boi_mais_gordo, maior_peso = verificar_boi_mais_gordo(identificacao, peso, boi_mais_gordo, maior_peso)
    
    mostrar_resultados(boi_mais_magro, menor_peso, boi_mais_gordo, maior_peso)

main()

#Foi feita uma pesquisa de audiência de canal de TV em várias casas em Teresina, num certo dia. Para
#cada casa visitada, o entrevistado informou o número do canal (2, 4, 5, 7, 10) e o número de pessoas que
#estavam assistindo TV. Escreva um algoritmo que leia um número indeterminado de dados (terminando
#quando for lido um canal igual a zero) e calcule o percentual de audiência para cada emissora,
#mostrando ao final, o número de cada canal e sua respectiva audiência.

from Utils.io_utils import pedir_int, pedir_int_min_max

#Pede para que o usuário digite um canal de uma lista específica de canais
def pedir_canal():
    canal_informado = pedir_int('Digite o canal que você está assistindo: ')

    if (canal_informado == 2 or canal_informado == 4 or canal_informado == 5 or canal_informado == 7 
    or canal_informado == 10 or canal_informado == 0):
        return canal_informado
    
    return pedir_canal()

#Calcula o percentual da audiência de um canal específico em relação às audiências de todos os outros canais
def calcular_percentual_de_audiencia(telespectadores_especificos, telespectadores_totais):
    return telespectadores_especificos / telespectadores_totais * 100

#Mostra os resultados encontrados pela pesquisa de audiência
def mostrar_resultados(telespectadores_totais, telespectadores_canal2, telespectadores_canal4, telespectadores_canal5,
telespectadores_canal7, telespectadores_canal10, percentual_canal2, percentual_canal4, percentual_canal5, 
percentual_canal7, percentual_canal10):
    print('\n======================== RESULTADOS ========================')
    print(f'\nTotal de telespectadores: {telespectadores_totais}')
    print(f'Audiência do canal 2: {telespectadores_canal2} telespectadores ({percentual_canal2:.2f} %)')
    print(f'Audiência do canal 4: {telespectadores_canal4} telespectadores ({percentual_canal4:.2f} %)')
    print(f'Audiência do canal 5: {telespectadores_canal5} telespectadores ({percentual_canal5:.2f} %)')
    print(f'Audiência do canal 7: {telespectadores_canal7} telespectadores ({percentual_canal7:.2f} %)')
    print(f'Audiência do canal 10: {telespectadores_canal10} telespectadores ({percentual_canal10:.2f} %)')

def main():
    cont = 0
    canal_informado = -1
    telespectadores_totais = 0
    telespectadores_canal2, telespectadores_canal4, telespectadores_canal5 = 0, 0, 0
    telespectadores_canal7, telespectadores_canal10 = 0, 0

    print('============================ IBOPE ============================')

    while canal_informado != 0:
        print(f'\nCasa {cont + 1}')
        canal_informado = pedir_canal()

        if canal_informado != 0:
            telespectadores_do_canal = pedir_int_min_max('Digite a quantidade de pessoas que estão assistindo: ', 1, 30)

            if canal_informado == 2:
                telespectadores_canal2 += telespectadores_do_canal
            elif canal_informado == 4:
                telespectadores_canal4 += telespectadores_do_canal
            elif canal_informado == 5:
                telespectadores_canal5 += telespectadores_do_canal
            elif canal_informado == 7:
                telespectadores_canal7 += telespectadores_do_canal
            else:
                telespectadores_canal10 += telespectadores_do_canal

            telespectadores_totais += telespectadores_do_canal

        cont += 1

    percentual_canal2 = calcular_percentual_de_audiencia(telespectadores_canal2, telespectadores_totais)
    percentual_canal4 = calcular_percentual_de_audiencia(telespectadores_canal4, telespectadores_totais)
    percentual_canal5 = calcular_percentual_de_audiencia(telespectadores_canal5, telespectadores_totais)
    percentual_canal7 = calcular_percentual_de_audiencia(telespectadores_canal7, telespectadores_totais)
    percentual_canal10 = calcular_percentual_de_audiencia(telespectadores_canal10, telespectadores_totais)

    mostrar_resultados(telespectadores_totais, telespectadores_canal2, telespectadores_canal4, telespectadores_canal5,
    telespectadores_canal7, telespectadores_canal10, percentual_canal2, percentual_canal4, percentual_canal5, 
    percentual_canal7, percentual_canal10)

main()

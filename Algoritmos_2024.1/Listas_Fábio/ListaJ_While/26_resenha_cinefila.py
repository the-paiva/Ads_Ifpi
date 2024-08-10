#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
#em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo). Escreva um algoritmo que leia a idade e
#a opinião das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
#· a média das idades das pessoas que responderam ótimo;
#· a quantidade de pessoas que respondeu regular;
#· o percentual de pessoas que respondeu bom entre os entrevistados.

from Utils.io_utils import pedir_int, pedir_int_min_max

#Escreve um cabeçalho informativo sobre o programa
def escrever_cabecalho():
    print('==================== AVALIAÇÕES ====================')
    print('1 - Ótimo')
    print('2 - Bom')
    print('3 - Regular')
    print('4 - Péssimo')
    print('====================================================')

#Pede a idade do espectador
def pedir_idade():
    idade = pedir_int('Digite sua idade: ')

    if (idade >= 4 and idade <= 120) or idade == -1:
        return idade
    
    return pedir_idade()

#Calcula a média de idade dos entrevistados que avaliaram o filme como ÓTIMO
def calcular_media_de_idades_de_otimo(somatorio_de_idades_de_otimo, quant_otimo):
    if quant_otimo >= 1:
        return somatorio_de_idades_de_otimo / quant_otimo
    
    return 0

#Mostra os resultados da pesquisa de avaliações
def mostrar_resultados(media_de_otimo, quant_regular, percentual_de_bom):
    print('\n=================== RESULTADOS ===========================')
    print(f'Média de idade de quem respondeu ÓTIMO: {media_de_otimo:.0f} anos')
    print(f'Quantidade de pessoas que responderam REGULAR: {quant_regular} pessoas')
    print(f'Percentual de pessoas que responderam BOM: {percentual_de_bom:.2f} %')
    print('===========================================================')

def main():
    idade = 0
    quant_entrevistados = 0
    quant_otimo, quant_regular, quant_bom, somatorio_de_idades_de_otimo = 0, 0, 0, 0

    escrever_cabecalho()

    while idade != -1:
        print(f'\nEspectador {quant_entrevistados + 1}')
        idade = pedir_idade()

        if idade != -1:
            opiniao = pedir_int_min_max('Digite uma avaliação sobre o filme: ', 1, 4)

            if opiniao == 1:
                quant_otimo += 1
                somatorio_de_idades_de_otimo += idade
            elif opiniao == 3:
                quant_regular += 1
            elif opiniao == 2:
                quant_bom += 1

        quant_entrevistados += 1

    percentual_de_bom = (quant_bom / quant_entrevistados) * 100
    media_de_otimo = calcular_media_de_idades_de_otimo(somatorio_de_idades_de_otimo, quant_otimo)

    mostrar_resultados(media_de_otimo, quant_regular, percentual_de_bom)

main()

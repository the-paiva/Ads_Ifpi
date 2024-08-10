#Escreva um algoritmo que leia um conjunto de dados de um grupo de 100 pessoas, sexo (1=Masculino,
#2=Feminino), idade e estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo) e escreva:
#· Média de idade das mulheres;
#· Média de idade dos homens;
#· O percentual de homens solteiros;
#· O percentual de mulheres solteiras;
#· A quantidade de mulheres divorciadas acima de 30 anos.

#O.B.S: Para fins de teste, deixei a quantidade de entrevistados por escolha do usuário

from Utils.io_utils import pedir_int_min_max
from Utils.math_utils import calcular_media_aritmetica

#Escreve um cabeçalho informativo sobre o programa
def escrever_cabecalho():
    print('\n==========================================================================')
    print('SEXO: 1 - Masculino; 2 - Feminino')
    print('ESTADO CIVIL: 1 - Casado; 2 - Solteiro; 3 - Divorciado; 4 - Viúvo')
    print('==========================================================================')

#Quantifica um determinado grupo de entrevistados de acordo com o estado civil informado
def quantificar_estado_civil(estado_civil_do_entrevistado, estado_civil_procurado, quantidade_atual):
    if estado_civil_do_entrevistado == estado_civil_procurado:
        return quantidade_atual + 1
    
    return quantidade_atual

#Mostra os resultados obtidos pela pesquisa
def mostrar_resultados(media_de_idade_das_mulheres, media_de_idade_dos_homens, percentual_de_homens_solteiros, 
percentual_de_mulheres_solteiras, quant_mulheres_divorciadas_acima_de_30):
    print('\n============================ RESULTADOS ===================================')
    print(f'Média de idade das mulheres: {media_de_idade_das_mulheres:.0f} anos')
    print(f'Média de idade dos homens: {media_de_idade_dos_homens:.0f} anos')
    print(f'Percentual de mulheres solteiras: {percentual_de_mulheres_solteiras:.2f} %')
    print(f'Percentual de homens solteiros: {percentual_de_homens_solteiros:.0f} % ')
    print(f'Quantidade de mulheres divorciadas acima dos 30 anos: {quant_mulheres_divorciadas_acima_de_30} mulheres')

def main():
    quant_entrevistados = pedir_int_min_max('Digite quantas pessoas serão entrevistadas (até 100): ', 1, 100)
    cont = 0
    soma_de_idade_das_mulheres, quant_mulheres, soma_de_idade_dos_homens, quant_homens = 0, 0, 0, 0
    quant_mulheres_solteiras, quant_homens_solteiros, quant_mulheres_divorciadas_acima_de_30 = 0, 0, 0

    escrever_cabecalho()

    while cont < quant_entrevistados:
        print(f'\nENTREVISTADO(A) {cont + 1}')
        sexo = pedir_int_min_max('Digite seu sexo: ', 1, 2)
        idade = pedir_int_min_max('Digite sua idade: ', 14, 130)
        estado_civil = pedir_int_min_max('Digite seu estado civil: ', 1, 4)

        if sexo == 2:
            soma_de_idade_das_mulheres += idade
            quant_mulheres += 1

            quant_mulheres_solteiras = quantificar_estado_civil(estado_civil, 2, quant_mulheres_solteiras)

            if estado_civil == 3 and idade > 30:
                quant_mulheres_divorciadas_acima_de_30 += 1
        elif sexo == 1:
            soma_de_idade_dos_homens += idade
            quant_homens += 1

            quant_homens_solteiros = quantificar_estado_civil(estado_civil, 2, quant_homens_solteiros)
        cont += 1

    media_de_idade_das_mulheres = calcular_media_aritmetica(soma_de_idade_das_mulheres, quant_mulheres)
    media_de_idade_dos_homens = calcular_media_aritmetica(soma_de_idade_dos_homens, quant_homens)
    percentual_de_mulheres_solteiras = quant_mulheres_solteiras / quant_mulheres * 100
    percentual_de_homens_solteiros = quant_homens_solteiros / quant_homens * 100

    mostrar_resultados(media_de_idade_das_mulheres, media_de_idade_dos_homens, percentual_de_homens_solteiros, 
    percentual_de_mulheres_solteiras, quant_mulheres_divorciadas_acima_de_30)

main()

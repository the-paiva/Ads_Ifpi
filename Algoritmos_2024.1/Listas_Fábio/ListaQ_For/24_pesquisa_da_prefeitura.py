#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
#número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
#escreva:
#a) média de salário da população;
#b) média de número de filhos;
#c) percentual de pessoas com salário de até R$ 1.000,00.

from Utils.io_utils import pedir_int_min, pedir_float_min
from Utils.math_utils import calcular_media_aritmetica

#Obtém o salário e a quantidade de filhos de um entrevistado
def obter_dados_do_entrevistado(cont):
    print(f'\n{cont + 1}ª ENTREVISTA')
    salario_do_entrevistado = pedir_float_min('-> Digite o seu salário: R$ ', 0)
    quant_filhos_do_entrevistado = pedir_int_min('-> Digite quantos filhos você tem: ', 0)

    return salario_do_entrevistado, quant_filhos_do_entrevistado

#Mostra os resultados obtidos pela pesquisa
def mostrar_resultados(media_de_salarios, media_de_filhos, percentual_de_salario_ate_1000):
    print('\nRELATÓRIO DE PESQUISA')
    print(f'Média de salário da população: R$ {media_de_salarios:.2f}')
    print(f'Média de filhos da população: {media_de_filhos:.0f}')
    print(f'Percentual de pessoas com salário de até R$ 1000,00: {percentual_de_salario_ate_1000:.2f} %')

def main():
    quant_entrevistados = pedir_int_min('-> Digite a quantidade de habitantes a serem entrevistados: ', 1)
    somatorio_de_salarios, somatorio_de_filhos = 0, 0
    quant_salario_ate_1000 = 0

    for cont in range(quant_entrevistados):
        salario_do_entrevistado, quant_filhos_do_entrevistado = obter_dados_do_entrevistado(cont)
        somatorio_de_salarios += salario_do_entrevistado
        somatorio_de_filhos += quant_filhos_do_entrevistado

        if salario_do_entrevistado <= 1000:
            quant_salario_ate_1000 += 1

    media_de_salarios = calcular_media_aritmetica(somatorio_de_salarios, quant_entrevistados)
    media_de_filhos = calcular_media_aritmetica(somatorio_de_filhos, quant_entrevistados)
    percentual_de_salario_ate_1000 = quant_salario_ate_1000 / quant_entrevistados * 100

    mostrar_resultados(media_de_salarios, media_de_filhos, percentual_de_salario_ate_1000)

main()

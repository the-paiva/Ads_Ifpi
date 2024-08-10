#Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
#crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
#crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
#necessários, para que a população da cidade A ultrapasse a população da cidade B.

#Pede uma entrada vazia ao usuário para iniciar a simulação
def iniciar_simulacao():
    input('Pressione ENTER para iniciar a simulação: ')
    print('\n==========================================================================')

#Mostra a diferença entre as populações das cidades em apenas um ano específico
def detalhar_ano_individual(ano, populacao_a, populacao_b):
    print(f'\nAno: {ano}')
    print(f'População da cidade A: {populacao_a:.0f}')
    print(f'População da cidade B: {populacao_b:.0f}')

#Encerra a simulação com uma mensagem informativa
def encerrar_simulacao(ano, anos_necessarios):
    print('\n==========================================================================')
    print(f'\nA população da cidade A ultrapassará a população da cidade B no ano {ano}.')
    print(f'Sendo assim, serão necessários {anos_necessarios} anos para que isso aconteça.')

def main():
    populacao_a = 200_000
    crescimento_da_populacao_a = 3.5 / 100

    populacao_b = 800_000
    crescimento_da_populacao_b = 1.35 / 100

    ano = 2023
    anos_necessarios = 0
    iniciar_simulacao()

    while populacao_a <= populacao_b:
        ano += 1
        anos_necessarios += 1

        populacao_a += populacao_a * crescimento_da_populacao_a
        populacao_b += populacao_b * crescimento_da_populacao_b
        detalhar_ano_individual(ano, populacao_a, populacao_b)

    encerrar_simulacao(ano, anos_necessarios)

main()

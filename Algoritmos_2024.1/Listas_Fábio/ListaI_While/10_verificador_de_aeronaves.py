#Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique
#se a aeronave pode levantar vôo ou não. Considere os seguintes critérios:
#· O peso de decolagem da aeronave é sempre igual a 500.000 kg;
#· O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
#passageiros;
#· O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
#· A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
#· O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
#· O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
#bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
#estimado de 10kg.
#O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
#ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
#bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
#de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
#mensagem indicando a liberação da decolagem ou não.

from Utils.io_utils import pedir_float_min, pedir_int_min

#Realiza a soma do peso dos containers da aeronave
def calcular_peso_dos_containers(quant_containers):
    cont_containers, peso_dos_containers = 0, 0

    while cont_containers < quant_containers:
        peso_dos_containers += pedir_float_min(f'Digite o peso do {cont_containers + 1}º container (em kg): ', 1000)
        cont_containers += 1

    return peso_dos_containers

#Pede o número de bilhete e a quantidade de bagagens de todos os passageiros
def pedir_dados_dos_passageiros():
    cont_passageiros, quant_bagagens = 0, 0
    numero_do_bilhete_atual = -1

    while numero_do_bilhete_atual != 0:
        numero_do_bilhete_atual = pedir_int_min('\nDigite o número do bilhete de algum passageiro: ', 0)

        if numero_do_bilhete_atual != 0:
            quant_bagagens += pedir_int_min('Digite a quantidade de bagagens do passageiro: ', 0)
            cont_passageiros += 1

    return cont_passageiros, quant_bagagens
    
#Analisa a situação do voo de acordo com sua quantidade de peso
def analisar_situacao_do_voo(peso_total, peso_de_decolagem):
    if peso_total <= peso_de_decolagem:
        return 'LIBERADO'
    else:
        return 'NÃO LIBERADO'

#Mostra um relatório com informações sobre o voo, inclusive se foi liberado ou não
def mostrar_relatorio(cont_passageiros, peso_das_bagagens, peso_dos_passageiros, peso_dos_containers,
peso_do_combustivel, peso_total, peso_de_decolagem, situacao_do_voo):
    print('\n======================= Relatório =======================')
    print(f'Quantidade de passageiros: {cont_passageiros}')
    print(f'Peso das bagagens: {peso_das_bagagens:.2f} kg')
    print(f'Peso dos passageiros: {peso_dos_passageiros:.2f} kg')
    print(f'Peso da carga: {peso_dos_containers:.2f} kg')
    print(f'Peso do combustível: {peso_do_combustivel:.2f} kg')
    print(f'Peso total: {peso_total:.2f} kg')
    print(f'Peso máximo para decolagem: {peso_de_decolagem} kg')
    print(f'Situação do vôo: {situacao_do_voo}')
    print('=========================================================')

def main():
    QUANT_MINIMA_DE_COMBUSTIVEL = 10000
    quant_combustivel = pedir_float_min('Digite a quantidade de combustível disponível (em litros): ', 1)

    if quant_combustivel >= QUANT_MINIMA_DE_COMBUSTIVEL:
        quant_containers = pedir_int_min('Digite a quantidade de containers que serão levados: ', 0)

        peso_dos_containers = calcular_peso_dos_containers(quant_containers)
        cont_passageiros, quant_bagagens = pedir_dados_dos_passageiros()
        peso_do_combustivel = quant_combustivel * 1.5

        peso_dos_passageiros = 70 * cont_passageiros
        peso_das_bagagens = 10 * quant_bagagens
        peso_total = peso_dos_containers + peso_do_combustivel + peso_dos_passageiros + peso_das_bagagens
        PESO_DE_DECOLAGEM = 500000

        situacao_do_voo = analisar_situacao_do_voo(peso_total, PESO_DE_DECOLAGEM)

        mostrar_relatorio(cont_passageiros, peso_das_bagagens, peso_dos_passageiros, peso_dos_containers,
        peso_do_combustivel, peso_total, PESO_DE_DECOLAGEM, situacao_do_voo)
    else:
        print('\nA quantidade mínima de combustível para a liberação do vôo não foi atingida!')

main()

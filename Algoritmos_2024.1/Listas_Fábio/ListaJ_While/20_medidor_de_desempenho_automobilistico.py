#Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
#600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
#um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
#· Distância percorrida desde a última medição;
#· Quantidade de litros consumidos para percorrer a distância indicada.
#Escreva um algoritmo que leia estas informações e escreva:
#· se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
#· se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
#· o consumo em km/l do carro.

from Utils.io_utils import pedir_float_min_max

#Calcula o consumo do carro em quilômetros por litro
def calcular_km_por_litro(distancia_percorrida, combustivel_consumido):
    if combustivel_consumido > 0:
        return distancia_percorrida / combustivel_consumido
    
    return 0

#Atribui a uma string uma mensagem que informa se o carro chegou ou não ao seu destino
def atribuir_mensagem_de_chegada(distancia_percorrida):
    if distancia_percorrida == 600:
        return 'O carro CHEGOU ao seu destino!'
    
    return 'O carro NÃO chegou ao seu destino!'

#Mostra os resultados relativos à viagem
def mostrar_resultados(distancia_percorrida, combustivel_consumido, km_por_litro, mensagem_de_chegada):
    print(f'\nDistância percorrida: {distancia_percorrida:.2f} Km')
    print(f'Combustível consumido: {combustivel_consumido:.2f} l')
    print(f'Consumo em km/l: {km_por_litro:.2f} km/l')
    print(f'\n{mensagem_de_chegada}')

def main():
    distancia_percorrida = 0 #Em Km
    combustivel_consumido = 0 #Em litros
    quant_medicoes = 0
    DISTANCIA_MAXIMA = 600
    TANQUE_CHEIO = 50

    while distancia_percorrida < 600 and combustivel_consumido < 50:
        quant_medicoes += 1
        distancia_restante = DISTANCIA_MAXIMA - distancia_percorrida
        combustivel_restante = TANQUE_CHEIO - combustivel_consumido

        print(f'\n{quant_medicoes}ª MEDIÇÃO')
        print(f'Distância restante: {distancia_restante:.2f} Km')
        print(f'Combustível restante: {combustivel_restante:.2f} l')

        distancia_percorrida += pedir_float_min_max('Digite a distância percorrida desde a última medição (em Km): ', 
        0, distancia_restante)

        combustivel_consumido += pedir_float_min_max('Digite quantos litros foram consumidos desde a última medição: ',
        0, combustivel_restante)
    
    km_por_litro = calcular_km_por_litro(distancia_percorrida, combustivel_consumido)
    mensagem_de_chegada = atribuir_mensagem_de_chegada(distancia_percorrida)

    mostrar_resultados(distancia_percorrida, combustivel_consumido, km_por_litro, mensagem_de_chegada)

main()

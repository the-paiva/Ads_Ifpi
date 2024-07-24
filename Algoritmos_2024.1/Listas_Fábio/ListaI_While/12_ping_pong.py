#Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de ping-pongue, e
#responda quem ganha a partida. A partida chega ao final se:
#· Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
#· Se a primeira condição não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar 
#uma diferença de 2 pontos sobre o adversário.

from Utils.io_utils import pedir_int_min_max

#Verifica se o jogo deve ou não continuar
def continuidade_de_jogo(pontos_do_jogador1, pontos_do_jogador2, diferenca_de_pontos):
    if (pontos_do_jogador1 >= 21 and diferenca_de_pontos >= 2) or (pontos_do_jogador2 >= 21
    and diferenca_de_pontos >= 2):
        return False
    
    return True

#Atribui pontos de acordo com o código de jogador digitado
def atribuir_pontos(cod_jogador, pontos_do_jogador1, pontos_do_jogador2):
    if cod_jogador == 1:
        return pontos_do_jogador1 + 1, pontos_do_jogador2
    
    return pontos_do_jogador1, pontos_do_jogador2 + 1

#Calcula a diferença de pontos entre os jogadores
def calcular_diferenca_de_pontos(pontos_do_jogador1, pontos_do_jogador2):
    if pontos_do_jogador1 >= pontos_do_jogador2:
        return pontos_do_jogador1 - pontos_do_jogador2
    
    return pontos_do_jogador2 - pontos_do_jogador1

#Atualiza o placar a cada atribuição de ponto dos jogadores
def mostrar_placar_atual(pontos_do_jogador1, pontos_do_jogador2, diferenca_de_pontos):
    print(f'\nPontos do jogador 1: {pontos_do_jogador1}')
    print(f'Pontos do jogador 2: {pontos_do_jogador2}')
    print(f'Diferença: {diferenca_de_pontos}\n')

#Atribui o vencedor do jogo a uma string com base na quantidade de pontos de cada jogador
def atribuir_vencedor_do_jogo(pontos_do_jogador1, pontos_do_jogador2):
    if pontos_do_jogador1 > pontos_do_jogador2:
        return 'JOGADOR 1'
    
    return 'JOGADOR 2'

def main():
    print('========================= PING-PONG =========================')

    pontos_do_jogador1, pontos_do_jogador2, diferenca_de_pontos = 0, 0, 0

    while continuidade_de_jogo(pontos_do_jogador1, pontos_do_jogador2, diferenca_de_pontos):
        cod_jogador = pedir_int_min_max('Digite o código do jogador: ', 1, 2)

        pontos_do_jogador1, pontos_do_jogador2 = atribuir_pontos(cod_jogador, pontos_do_jogador1, 
        pontos_do_jogador2)

        diferenca_de_pontos = calcular_diferenca_de_pontos(pontos_do_jogador1, pontos_do_jogador2)

        mostrar_placar_atual(pontos_do_jogador1, pontos_do_jogador2, diferenca_de_pontos)

    vencedor_do_jogo = atribuir_vencedor_do_jogo(pontos_do_jogador1, pontos_do_jogador2)
    print(f'O {vencedor_do_jogo} venceu o jogo!')

main()

#Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
#prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
#quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
#clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:
#
#Lugar    Pontos
# 1         9
# 2         6
# 3         4
# 4         3
#
#Ao final, o algoritmo deve escrever os totais de pontos de cada clube, indicando o clube vencedor.

from Utils.io_utils import pedir_int_min, pedir_string, pedir_float_min_max, pedir_int_min_max

#Entra em um loop que pede o clube do nadador até obter como resposta 'a' ou 'b'
def pedir_clube_do_nadador(nome_do_nadador):
    clube_do_nadador = pedir_string(f'Digite qual o clube de {nome_do_nadador}: ').lower()

    if clube_do_nadador == 'a' or clube_do_nadador == 'b':
        return clube_do_nadador
    
    return pedir_clube_do_nadador(nome_do_nadador)

#Calcula a pontuação do nadador de acordo com sua classificação
def calcular_pontuacao_do_nadador(classificacao_do_nadador):
    if classificacao_do_nadador == 1:
        return 9
    elif classificacao_do_nadador == 2:
        return 6
    elif classificacao_do_nadador == 3:
        return 4
    
    return 3

#Atualiza a pontuação dos clubes de acordo com a última pontuação registrada de um nadador
def atualizar_pontuacao_dos_clubes(clube_do_nadador, pontuacao_do_nadador, pontuacao_do_clube_a,
pontuacao_do_clube_b):
    if clube_do_nadador == 'a':
        return pontuacao_do_clube_a + pontuacao_do_nadador, pontuacao_do_clube_b
    
    return pontuacao_do_clube_a, pontuacao_do_clube_b + pontuacao_do_nadador

#Verifica qual clube foi vencedor da corrida ou se houve empate
def processar_resultado(pontuacao_do_clube_a, pontuacao_do_clube_b):
    if pontuacao_do_clube_a > pontuacao_do_clube_b:
        return 'O clube a foi o vencedor'
    elif pontuacao_do_clube_b > pontuacao_do_clube_a:
        return 'O clube b foi o vencedor'
    
    return 'Empate'

#Escreve o resultado final da disputa
def mostrar_resultado(pontuacao_do_clube_a, pontuacao_do_clube_b, resultado):
    print('\n==================== FIM DA CORRIDA ====================')
    print(f'Pontuação do clube a: {pontuacao_do_clube_a}')
    print(f'Pontuação do clube b: {pontuacao_do_clube_b}')
    print(f'Resultado: {resultado}')

def main():
    num_prova, num_nadadores = -1, -1
    pontuacao_do_clube_a, pontuacao_do_clube_b = 0, 0

    while num_prova != 0 and num_nadadores != 0:
        num_prova = pedir_int_min('\nDigite o número da prova: ', 0)
        num_nadadores = pedir_int_min('Digite a quantidade de nadadores que disputarão a prova: ', 0)
        
        if num_prova != 0 and num_nadadores != 0:
            cont = 0

            while cont < num_nadadores:
                nome_do_nadador = pedir_string(f'\nDigite o nome do {cont + 1}º nadador: ').upper()
                classificacao_do_nadador = pedir_int_min_max(f'Digite a classificação de {nome_do_nadador}: ', 
                min = 1, max = 4)
                tempo_do_nadador = pedir_float_min_max(f'Digite o tempo de corrida de {nome_do_nadador} (em segundos): ', 
                min = 1, max = 1200)
                clube_do_nadador = pedir_clube_do_nadador(nome_do_nadador)

                pontuacao_do_nadador = calcular_pontuacao_do_nadador(classificacao_do_nadador)
                pontuacao_do_clube_a, pontuacao_do_clube_b = atualizar_pontuacao_dos_clubes(clube_do_nadador,
                pontuacao_do_nadador, pontuacao_do_clube_a, pontuacao_do_clube_b)

                cont += 1

    resultado = processar_resultado(pontuacao_do_clube_a, pontuacao_do_clube_b)
    mostrar_resultado(pontuacao_do_clube_a, pontuacao_do_clube_b, resultado)

main()

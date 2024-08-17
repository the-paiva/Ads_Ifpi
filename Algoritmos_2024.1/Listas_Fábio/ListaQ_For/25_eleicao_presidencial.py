#Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
#Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
#· 1, 2, 3 = voto para os respectivos candidatos;
#· 9 = voto nulo;
#· 0 = voto em branco;
#Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
#a) total de votos para cada candidato;
#b) total de votos nulos;
#c) total de votos em branco;
#d) quem venceu a eleição.

#O.B.S: O cenário de um possível segundo turno foi ignorado aqui

from Utils.io_utils import pedir_int, pedir_int_min

#Escreve o cabeçalho do programa
def escrever_cabecalho():
    print('\n========================================================================')
    print('Para votar no candidato ROGÉRIO SILVA digite 1')
    print('Para votar no candidato RICARDO RAMOS digite 2')
    print('Para votar no candidato FRANCISCO MARCELINO digite 3')
    print('Para votar NULO digite 9')
    print('Para votar em BRANCO digite 0')
    print('=========================================================================')

#Pede a intenção de voto do pesquisado, aceitando apenas números válidos da eleição
def pedir_intencao_de_voto(cont):
    print(f'\nEleitor {cont + 1}')
    intencao_de_voto = pedir_int('Digite sua intenção de voto para essas eleições: ')

    if (intencao_de_voto == 1 or intencao_de_voto == 2 or intencao_de_voto == 3 or
    intencao_de_voto == 9 or intencao_de_voto == 0):
        return intencao_de_voto
    
    return pedir_intencao_de_voto(cont)

#Atribui o resultado final da eleição a uma string
def retornar_resultado_da_eleicao(votos_do_rogerio, votos_do_ricardo, votos_do_marcelino):
    if votos_do_rogerio > votos_do_ricardo and votos_do_rogerio > votos_do_marcelino:
        return 'O candidato ROGÉRIO SILVA venceu as eleições'
    elif votos_do_ricardo > votos_do_rogerio and votos_do_ricardo > votos_do_marcelino:
        return 'O candidato RICARDO RAMOS venceu as eleições'
    elif votos_do_marcelino > votos_do_rogerio and votos_do_marcelino > votos_do_ricardo:
        return 'O candidato FRANCISCO MARCELINO venceu as eleições'
    
    return 'As eleições resultaram em EMPATE'

#Mostra o resultado da eleição
def mostrar_resultado(votos_do_rogerio, votos_do_ricardo, votos_do_marcelino, votos_nulos, votos_brancos, resultado_da_eleicao):
    print('\n========================================================================')
    print(f'Votos do ROGÉRIO: {votos_do_rogerio}')
    print(f'Votos do RICARDO: {votos_do_ricardo}')
    print(f'Votos do MARCELINO: {votos_do_marcelino}')
    print(f'Votos NULOS: {votos_nulos}')
    print(f'Votos em BRANCO: {votos_brancos}')
    print(f'\n{resultado_da_eleicao}')

def main():
    quant_eleitores = pedir_int_min('Digite a quantidade de eleitores a serem entrevistados: ', 1)
    votos_do_rogerio, votos_do_ricardo, votos_do_marcelino, votos_nulos, votos_brancos = 0, 0, 0, 0, 0

    escrever_cabecalho()

    for cont in range(quant_eleitores):
        intencao_de_voto = pedir_intencao_de_voto(cont)

        if intencao_de_voto == 1:
            votos_do_rogerio += 1
        elif intencao_de_voto == 2:
            votos_do_ricardo += 1
        elif intencao_de_voto == 3:
            votos_do_marcelino += 1
        elif intencao_de_voto == 9:
            votos_nulos += 1
        else:
            votos_brancos += 1

    resultado_da_eleicao = retornar_resultado_da_eleicao(votos_do_rogerio, votos_do_ricardo, votos_do_marcelino)

    mostrar_resultado(votos_do_rogerio, votos_do_ricardo, votos_do_marcelino, votos_nulos, votos_brancos, resultado_da_eleicao)

main()

#Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
#entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
#responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
#entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
#· a porcentagem de cada candidato;
#· a porcentagem dos outros candidatos;
#· a porcentagem de eleitores indecisos;
#· a porcentagem de votos nulos/brancos;
#· o total de entrevistados;
#· uma mensagem indicando a possibilidade ou não de haver 2º turno.

from Utils.io_utils import pedir_int

#Escreve o cabeçalho do programa
def escrever_cabecalho():
    print('========================= PESQUISA DO DATAFOLHA =========================')
    print('Para votar no candidato SERRA digite 45')
    print('Para votar na candidata DILMA digite 13')
    print('Para votar no candidato CIRO GOMES digite 23')
    print('Para votar em OUTROS candidatos digite 98')
    print('Para votar NULO/BRANCO digite 0')
    print('Caso esteja INDECISO em relação ao seu voto digite 99')
    print('Para encerrar o sistema de pesquisa digite -1')
    print('=========================================================================')

#Pede a intenção de voto do pesquisado, aceitando apenas números válidos da eleição
def pedir_intencao_de_voto():
    intencao_de_voto = pedir_int('Digite sua intenção de voto para essas eleições: ')

    if (intencao_de_voto == 45 or intencao_de_voto == 13 or intencao_de_voto == 23 or
    intencao_de_voto == 99 or intencao_de_voto == 98 or intencao_de_voto == 0 or intencao_de_voto == -1):
        return intencao_de_voto
    
    return pedir_intencao_de_voto()

#Calcula a porcentagem de votos de um candidato específico
def calcular_porcentagem_de_votos(votos_especificos, quantidade_de_entrevistados):
    return (votos_especificos / quantidade_de_entrevistados) * 100

#Atribui uma mensagem a uma string de acordo com a chance de haver ou não um segundo turno
def atribuir_mensagem_sobre_segundo_turno(porcentagem_do_serra, porcentagem_da_dilma, porcentagem_do_ciro):
    if porcentagem_do_serra > 50 or porcentagem_da_dilma > 50 or porcentagem_do_ciro > 50:
        return 'É IMPROVÁVEL que haja um segundo turno nessas eleições'
    
    return 'É PROVÁVEL que haja um segundo turno nessas eleições'

#Mostra o resultado final da pesquisa
def mostrar_resultado_da_pesquisa(porcentagem_do_serra, porcentagem_da_dilma, porcentagem_do_ciro,
porcentagem_de_outros, porcentagem_de_indecisos, porcentagem_de_nulo, quantidade_de_entrevistados,
mensagem_sobre_segundo_turno):
    print('======================= RESULTADO DA PESQUISA =======================')
    print(f'Porcentagem de votos do candidato SERRA: {porcentagem_do_serra:.2f} %')
    print(f'Porcentagem de votos da candidata DILMA: {porcentagem_da_dilma:.2f} %')
    print(f'Porcentagem de votos do candidato CIRO: {porcentagem_do_ciro:.2f} %')
    print(f'Porcentagem de votos dos OUTROS candidatos: {porcentagem_de_outros:.2f} %')
    print(f'Porcentagem de eleitores INDECISOS: {porcentagem_de_indecisos:.2f} %')
    print(f'Porcentagem de votos NULO/BRANCO: {porcentagem_de_nulo:.2f} %')
    print(f'Quantidade de entrevistados: {quantidade_de_entrevistados}')
    print(f'{mensagem_sobre_segundo_turno}')
    print('=====================================================================')

def main():
    escrever_cabecalho()
    intencao_de_voto = -2
    quantidade_de_entrevistados = 0
    votos_do_serra, votos_da_dilma, votos_do_ciro, votos_indecisos, votos_de_outros, votos_nulo = 0, 0, 0, 0, 0, 0

    while intencao_de_voto != -1:
        intencao_de_voto = pedir_intencao_de_voto()

        if intencao_de_voto != -1:
            quantidade_de_entrevistados += 1

            if intencao_de_voto == 45:
                votos_do_serra += 1
            elif intencao_de_voto == 13:
                votos_da_dilma += 1
            elif intencao_de_voto == 23:
                votos_do_ciro += 1
            elif intencao_de_voto == 99:
                votos_indecisos += 1
            elif intencao_de_voto == 98:
                votos_de_outros += 1
            else:
                votos_nulo += 1

    porcentagem_do_serra = calcular_porcentagem_de_votos(votos_do_serra, quantidade_de_entrevistados)
    porcentagem_da_dilma = calcular_porcentagem_de_votos(votos_da_dilma, quantidade_de_entrevistados)
    porcentagem_do_ciro = calcular_porcentagem_de_votos(votos_do_ciro, quantidade_de_entrevistados)
    porcentagem_de_outros = calcular_porcentagem_de_votos(votos_de_outros, quantidade_de_entrevistados)
    porcentagem_de_indecisos = calcular_porcentagem_de_votos(votos_indecisos, quantidade_de_entrevistados)
    porcentagem_de_nulo = calcular_porcentagem_de_votos(votos_nulo, quantidade_de_entrevistados)

    mensagem_sobre_segundo_turno = atribuir_mensagem_sobre_segundo_turno(porcentagem_do_serra, 
    porcentagem_da_dilma, porcentagem_do_ciro)

    mostrar_resultado_da_pesquisa(porcentagem_do_serra, porcentagem_da_dilma, porcentagem_do_ciro,
    porcentagem_de_outros, porcentagem_de_indecisos, porcentagem_de_nulo, quantidade_de_entrevistados,
    mensagem_sobre_segundo_turno)

main()

#Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima ?"
#b) "Esteve no local do crime ?"
#c) "Mora perto da vítima ?"
#d) "Devia para a vítima ?"
#e) "Já trabalhou com a vítima ?"
#O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
#responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
#"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

from Utils.io_utils import pedir_string
from time import sleep

#Escreve o cabeçalho do programa
def escrever_cabecalho():
    print('==================== Depoimento dos Reprovados ====================')
    print('Responda S para resposta afirmativa')
    print('Responda N para resposta negativa')
    print('===================================================================')

#Incrementa a quantidade de respostas positivas caso a resposta analisada também seja positiva
def incrementar_resposta_positiva(resposa_analisada):
    if (resposa_analisada == 's' or resposa_analisada == 'S'):
        return 1
    
    return 0

#Incrementa a quantidade de respostas válidas caso a resposta analisada também seja válida (S ou N)
def incrementar_resposta_valida(resposta_analisada):
    if (resposta_analisada == 's' or resposta_analisada == 'S' or resposta_analisada == 'n'
    or resposta_analisada == 'N'):
        return 1

    return 0

#Atribui a classificação de participação do interrogado a uma variável string
def retornar_classificacao_de_participacao(respostas_positivas):
    if respostas_positivas == 5:
        return 'ASSASSINO'
    elif respostas_positivas >= 3:
        return 'CÚMPLICE'
    elif respostas_positivas == 2:
        return 'SUSPEITO'
    
    return 'INOCENTE'

#Escreve na tela a classificação de participação no crime
def escrever_resultado(classificacao_de_participacao):
    print('===================================================================')
    print(f'Classificação de participação: {classificacao_de_participacao}')

#Encerra o programa com uma mensagem de erro
def erro():
    print(f'\nAlguma resposta digitada é inválida! Encerrando o programa...')
    sleep(3)

def main():
    escrever_cabecalho()

    respostas_positivas = 0
    respostas_validas = 0

    resposta_do_telefonema = pedir_string('Telefonou para a vítima? ')
    respostas_validas += incrementar_resposta_valida(resposta_do_telefonema)

    resposta_do_local = pedir_string('Esteve no local do crime? ')
    respostas_validas += incrementar_resposta_valida(resposta_do_local)

    resposta_da_moradia = pedir_string('Mora perto da vítima? ')
    respostas_validas += incrementar_resposta_valida(resposta_da_moradia)

    resposta_da_divida = pedir_string('Devia para a vítima? ')
    respostas_validas += incrementar_resposta_valida(resposta_da_divida)

    resposta_do_trabalho = pedir_string('Já trabalhou com a vítima? ')
    respostas_validas += incrementar_resposta_valida(resposta_do_trabalho)

    if respostas_validas == 5:
        respostas_positivas += incrementar_resposta_positiva(resposta_do_telefonema)
        respostas_positivas += incrementar_resposta_positiva(resposta_do_local)
        respostas_positivas += incrementar_resposta_positiva(resposta_da_moradia)
        respostas_positivas += incrementar_resposta_positiva(resposta_da_divida)
        respostas_positivas += incrementar_resposta_positiva(resposta_do_trabalho)
        classificacao_de_participacao = retornar_classificacao_de_participacao(respostas_positivas)

        escrever_resultado(classificacao_de_participacao)
    else:
        erro()

main()

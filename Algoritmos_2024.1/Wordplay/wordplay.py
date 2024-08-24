#Atividade U: Wordplay

#O.B.S: As funções mais genéricas ficaram no arquivo string_utils. Nesse arquivo, ficaram apenas as funções
#mais específicas da atividade

from Utils.io_utils import pedir_int_min_max, pedir_string
from Utils.string_utils import preparar_palavra, limpar_tela, enter_para_limpar_tela, tem_mais_letras, eh_letra_especifica

#Escreve um cabeçalho informativo sobre o funcionamento do programa
def escrever_cabecalho():
    print('\n=================================== WORDPLAY ===================================')
    print('| Arquivo de referência: words.txt')
    print('| Digite 1 para retornar apenas palavras com mais de 20 letras')
    print('| Digite 2 para retornar apenas palavras que não tenham a letra E')
    print('| Digite 3 para usar a função Avoids')
    print('| Digite 4 para usar a função Uses_only')
    print('| Digite 5 para usar a função Uses_all')
    print('| Digite 6 para usar a função Is_abecedarian')
    print('| Digite 0 para encerrar o programa')
    print('================================================================================')

#Retorna palavras com mais de 20 letras
def retornar_palavras_com_mais_de_20_letras():
    limpar_tela()

    fin = open('words.txt')
    print('\n================================================================================')
    print('Palavras com mais de 20 letras\n')

    for palavra in fin:
        palavra = preparar_palavra(fin)

        if tem_mais_letras(palavra, 20):
            print(f'- {palavra}'.upper())
    
    print('================================================================================')
    enter_para_limpar_tela()

#Retorna palavras que não têm a letra E
def retornar_palavras_sem_e():
    limpar_tela()

    fin = open('words.txt')
    print('\n================================================================================')
    print('Palavras sem a letra E\n')

    for palavra in fin:
        palavra = preparar_palavra(fin)

        if has_no_e(palavra):
            print(f'- {palavra}'.upper())

    print('================================================================================')
    enter_para_limpar_tela()

#Verifica se uma palavra contém a letra e
def has_no_e(palavra):
    for letra in palavra:
        if letra == 'e':
            return False
        
    return True

#Recebe uma série de letras proibidas, retornando quantas palavras do arquivo não contêm nenhuma delas
def avoids():
    limpar_tela()

    fin = open('words.txt')
    print('\n================================================================================')
    lista_de_letras = pedir_string('-> Digite uma série de letras que devem ser proibidas: ').strip().upper()

    estado_de_letra_proibida = False
    quant_palavras_sem_letras_proibidas = 0
    
    for palavra in fin:
        for letra in palavra:
            estado_de_letra_proibida = eh_letra_especifica(letra.upper(), lista_de_letras)

            if estado_de_letra_proibida == True:
                break

        if estado_de_letra_proibida == False:
            print(f'- {palavra}'.upper())
            quant_palavras_sem_letras_proibidas += 1

    print(f'Quantidade de palavras sem as letras proibidas: {quant_palavras_sem_letras_proibidas}')
    print('================================================================================')
    enter_para_limpar_tela()

#Recebe uma palavra e uma série de letras, sinalizando se a palavra contém ou não apenas as letras listadas
def uses_only():
    limpar_tela()

    print('\n================================================================================')
    lista_de_letras = pedir_string('-> Digite uma série de letras que devem ser selecionadas: ').strip().upper()
    palavra = pedir_string('-> Digite a palavra que será analisada: ').strip().upper()

    estado_de_letra_especifica = True
    mensagem = f'\n{palavra} é uma palavra que contém apenas as letras selecionadas'

    for letra in palavra:
        estado_de_letra_especifica = eh_letra_especifica(letra, lista_de_letras)
        
        if estado_de_letra_especifica == False:
            mensagem = f'\n{palavra} é uma palavra que NÃO contém apenas as letras selecionada'
            break

    print(mensagem)
    print('================================================================================')
    enter_para_limpar_tela()

#Recebe uma palavra e uma série de letras, sinalizando se a palavra usa ou não todas as letras da lista pelo menos uma vez
def uses_all():
    limpar_tela()

    print('\n================================================================================')
    lista_de_letras = pedir_string('-> Digite uma série de letras que devem ser selecionadas: ').strip().upper()
    palavra = pedir_string('-> Digite a palavra que será analisada: ').strip().upper()

    quant_letras_selecionadas_encontradas = 0
    mensagem = f'\n{palavra} usa todas as letras selecionadas'

    for letra in lista_de_letras:
        for letra_analisada in palavra:
            if letra_analisada == letra:
                quant_letras_selecionadas_encontradas += 1
                break

    if quant_letras_selecionadas_encontradas != len(lista_de_letras):
        mensagem = f'\n{palavra} NÃO usa todas as letras selecionadas'

    print(mensagem)
    print('================================================================================')
    enter_para_limpar_tela()

#Verifica se as letras de uma palavra estão em ordem alfabética
def is_abecedarian():
    limpar_tela()

    print('\n================================================================================')
    palavra = pedir_string('-> Digite uma palavra para ser analisada: ').strip().upper()

    estado_de_ordem_alfabetica = True
    mensagem = f'\n{palavra} tem as suas letras organizadas em ordem alfabética'

    for letra in range(len(palavra) - 1):
        if palavra[letra] > palavra[letra + 1]:
            estado_de_ordem_alfabetica = False

    if estado_de_ordem_alfabetica == False:
        mensagem = f'\n{palavra} não tem as suas letras organizadas em ordem alfabética'

    print(mensagem)
    print('================================================================================')
    enter_para_limpar_tela()

def main():
    digito = -1
    
    while digito != 0:
        escrever_cabecalho()
        digito = pedir_int_min_max('\n-> Digite uma das opções listadas: ', 0, 6)

        if digito == 1:
            retornar_palavras_com_mais_de_20_letras() #Exercício 9.1
        elif digito == 2:
            retornar_palavras_sem_e() #Exercício 9.2
        elif digito == 3:
            avoids() #Exercício 9.3
        elif digito == 4:
            uses_only() #Exercício 9.4
        elif digito == 5:
            uses_all() #Exercício 9.5
        elif digito == 6:
            is_abecedarian() #Exercício 9.6

main()

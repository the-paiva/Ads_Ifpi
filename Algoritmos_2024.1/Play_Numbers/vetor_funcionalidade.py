#Arquivo destinado às funções específicas da atividade V


from io_utils import pedir_int_min_max, pedir_int_min, pedir_float_min_max, pedir_float, pedir_float_min, pedir_int, pedir_string
from string_utils import limpar_tela, enter_para_limpar_tela
from math_utils import calcular_media_aritmetica, truncar_casas_decimais
from random import uniform
from os import path
import vetor_utils


#Variável que armazena a mensagem do menu principal do programa
MENSAGEM_DO_MENU_PRINCIPAL ='''
=========================================== PLAY NUMBER ===========================================
| Digite 1 para inicializar o vetor
| Digite 2 para mostrar os valores do vetor
| Digite 3 para resetar o vetor através de um valor padrão
| Digite 4 para ver a quantidade de itens do vetor
| Digite 5 para ver o menor e o maior valor do vetor
| Digite 6 para calcular o somatório dos itens do vetor
| Digite 7 para calcular a média aritmética dos valores
| Digite 8 para mostrar os valores positivos do vetor e sua quantidade
| Digite 9 para mostrar os valores negativos do vetor e sua quantidade
| Digite 10 para atualizar os valores do vetor por regras específicas
| Digite 11 para adicionar novos valores ao vetor já existente
| Digite 12 para remover um item do vetor de acordo com seu valor exato
| Digite 13 para remover um item do vetor de acordo com sua posição
| Digite 14 para editar o valor de um item do vetor de acordo com sua posição
| Digite 15 para salvar manualmente os valores do vetor em um arquivo .txt de sua escolha
| Digite 16 para sair do programa (os valores atuais serão salvos automaticamente em automatico.txt)
===================================================================================================
'''


#Variável que armazena a mensagem do sub-menu de inicialização de vetor
MENSAGEM_DE_INICIALIZACAO_DE_VETOR = '''
===================================================================================================
| Digite 1 para inicializar o vetor com valores aleatórios
| Digite 2 para inicializar o vetor com valores selecionados manualmente
| Digite 3 para inicializar o vetor a partir dos valores de um arquivo
===================================================================================================
'''


#Variável que armazena a mensagem do sub-menu de atualização do vetor por regras específicas
MENSAGEM_DE_ATUALIZACAO_REGRADA = '''
===================================================================================================
| Digite 1 para multiplicar todos os valores por um valor específico
| Digite 2 para elevar todos os valores a um valor específico (Exponenciação)
| Digite 3 para reduzir todos os valores a uma fração
| Digite 4 para trocar os valores negativos por um valor aleatório dentro do intervalo estabelecido
| Digite 5 para ordenar os valores de forma reversa
| Digite 6 para embaralhar os valores
===================================================================================================
'''


MENSAGEM_DE_VETOR_VAZIO = 'Não há valores no vetor analisado'
MENSAGEM_DE_VALORES_IGUAIS = 'Todos os valores do vetor são iguais'
MENSAGEM_DE_VETOR_POSITIVO_VAZIO = 'Não há valores positivos no vetor analisado'
MENSAGEM_DE_VETOR_NEGATIVO_VAZIO = 'Não há valores negativos no vetor analisado'
MENSAGEM_DE_VETOR_NAO_INICIALIZADO = 'O vetor ainda não foi inicializado'


#Menu principal do programa
def menu_principal():
    print(MENSAGEM_DO_MENU_PRINCIPAL)


#Primeira parte da estrutura padrão dos sub-menus do programa
def estrutura_inicial_de_sub_menu():
    limpar_tela()
    print('===================================================================================================')


#Segunda parte da estrutura padrão dos sub-menus do programa
def estrutura_final_de_sub_menu():
    print('===================================================================================================')
    enter_para_limpar_tela()


#Menu referente à inicialização de um vetor numérico de acordo com as especificações do usuário
def menu_de_inicializacao_de_vetor(CASAS_DECIMAIS):
    vetor = []
    CASAS_DECIMAIS = 2

    limpar_tela()
    print(MENSAGEM_DE_INICIALIZACAO_DE_VETOR)
    digito_de_geracao = pedir_int_min_max('-> Escolha uma das opções listadas acima: ', 1, 3)

    if digito_de_geracao == 1 or digito_de_geracao == 2:
        quant_elementos = pedir_int_min('-> Digite quantos elementos terão no vetor (no mínimo 1): ', 1)
        input_de_limite_inferior = '-> Digite o limite inferior do vetor: '
        input_de_limite_superior = '-> Digite o limite superior do vetor (não deve ser menor que o limite inferior): '
    else:
        input_de_limite_inferior = '-> Digite o NOVO limite inferior do vetor: '
        input_de_limite_superior = '-> Digite o NOVO limite superior do vetor (não deve ser menor que o limite inferior): '
    
    limite_inferior = pedir_float(input_de_limite_inferior)
    limite_superior = pedir_float_min(input_de_limite_superior, limite_inferior)

    if digito_de_geracao == 1:
        vetor = vetor_utils.inicializar_vetor_aleatoriamente_in_range(vetor, quant_elementos, limite_inferior, limite_superior)
    elif digito_de_geracao == 2:
        vetor = vetor_utils.inicializar_vetor_manualmente_in_range(vetor, quant_elementos, limite_inferior, limite_superior)
    else:
        print('O.B.S: Os novos limites inferior e superior NÃO afetam os valores já contidos no arquivo')
        nome_do_arquivo = pedir_nome_do_arquivo()
        vetor = vetor_utils.inicializar_vetor_com_arquivo(vetor, nome_do_arquivo)
        vetor = vetor_utils.converter_vetor_string_para_float(vetor)

    vetor = vetor_utils.truncar_casas_decimais_de_vetor(vetor, CASAS_DECIMAIS)

    estrutura_final_de_sub_menu()

    return vetor, limite_inferior, limite_superior


#Agregada de menu_de_inicializacao_de_vetor - Entra em um loop que pede pelo nome de um arquivo para ser carregado,
#cujos valores devem ser atribuidos em um vetor. O programa sai do loop quando o nome de um arquivo válido é informado
def pedir_nome_do_arquivo():
    while True:
        nome_do_arquivo = pedir_string('\nDigite o nome do arquivo (junto com o nome do formato): ')

        if path.exists(nome_do_arquivo):
            return nome_do_arquivo

        print('O nome de arquivo informado é INVÁLIDO! Tente novamente...')


#Menu referente ao relatório dos valores contidos no vetor analisado
def menu_de_relatorio_de_valores(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        vetor_utils.escrever_vetor_e_indices(vetor)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente ao processo de resetar os valores do vetor analisado
def menu_de_reset_de_valores(vetor, CASAS_DECIMAIS):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        vetor = vetor_utils.resetar_valores(vetor)
        vetor = vetor_utils.truncar_casas_decimais_de_vetor(vetor, CASAS_DECIMAIS)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)
    
    estrutura_final_de_sub_menu()

    return vetor


#Menu referente ao relatório da quantidade de elementos contidos no vetor analisado
def menu_de_quantidade_de_elementos(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        print(f'Quantidade de elementos: {len(vetor)}')
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)
    
    estrutura_final_de_sub_menu()


#Menu referente ao relatório do menor e do maior valor entre os valores contidos no vetor analisado
def menu_de_menor_e_maior_valor(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        menor_valor = vetor_utils.retornar_menor_valor_de_vetor(vetor)
        index_do_menor_valor = vetor_utils.retornar_index(vetor, menor_valor) + 1
        maior_valor = vetor_utils.retornar_maior_valor_de_vetor(vetor)
        index_do_maior_valor = vetor_utils.retornar_index(vetor, maior_valor) + 1

        if menor_valor != maior_valor:
            print(f'Menor valor: {menor_valor}\nMaior valor: {maior_valor}')
            print(f'\nPosição do menor valor: {index_do_menor_valor}º\nPosição do maior valor: {index_do_maior_valor}º')
        else:
            escrever_mensagem_de_erro(MENSAGEM_DE_VALORES_IGUAIS)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente ao somatório dos valores do vetor analisado
def menu_de_somatorio(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        somatorio = vetor_utils.calcular_somatorio(vetor)
        print(f'Somatório dos valores: {somatorio:.2f}')
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)
    
    estrutura_final_de_sub_menu()


#Menu referente à media aritmética dos valores do vetor analisado
def menu_de_media_aritmetica(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        somatorio = vetor_utils.calcular_somatorio(vetor)
        media_aritmetica = calcular_media_aritmetica(somatorio, len(vetor))
        print(f'Média aritmética dos valores: {media_aritmetica:.2f}')
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente ao relatório dos números positivos contidos no vetor analisado
def menu_de_numeros_positivos(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        vetor_de_positivos = vetor_utils.criar_vetor_de_positivos(vetor)

        if len(vetor_de_positivos) > 0:
            vetor_utils.escrever_vetor_e_indices(vetor_de_positivos)
            print(f'\nQuantidade total de números positivos: {len(vetor_de_positivos)}')
        else:
            escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_POSITIVO_VAZIO)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente ao relatório dos números negativos contidos no vetor analisado
def menu_de_numeros_negativos(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        vetor_de_negativos = vetor_utils.criar_vetor_de_negativos(vetor)

        if len(vetor_de_negativos) > 0:
            vetor_utils.escrever_vetor_e_indices(vetor_de_negativos)
            print(f'\nQuantidade total de números negativos: {len(vetor_de_negativos)}')
        else:
            escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_NEGATIVO_VAZIO)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente à atualização dos valores do vetor de acordo com regras específicas que podem ser escolhidas pelo usuário
def menu_de_atualizacao_regrada(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS):
    if len(vetor) > 0:
        limpar_tela()
        print(MENSAGEM_DE_ATUALIZACAO_REGRADA)
        digito = pedir_int_min_max('-> Digite uma das opções listadas acima: ', 1, 6)

        if digito == 1:
            multiplicador = pedir_float('\n-> Digite um valor para multiplicar os outros valores: ')
            vetor = vetor_utils.multiplicar_valores_de_vetor(vetor, multiplicador)
            vetor = vetor_utils.truncar_casas_decimais_de_vetor(vetor, CASAS_DECIMAIS)
        elif digito == 2:
            expoente = pedir_float('\n-> Digite o valor do expoente: ')
            vetor = vetor_utils.elevar_valores_de_vetor(vetor, expoente)
            vetor = vetor_utils.truncar_casas_decimais_de_vetor(vetor, CASAS_DECIMAIS)
        elif digito == 3:
            numerador = pedir_int('\n-> Digite o valor do numerador (inteiro): ')
            denominador = pedir_int_min('-> Digite agora o valor do denominador (inteiro maior que 0): ', 1)
            vetor = multiplicar_por_fracao(vetor, numerador, denominador, CASAS_DECIMAIS)
        elif digito == 4:
            vetor = substituir_negativos_aleatoriamente(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS)
        elif digito == 5:
            vetor = vetor_utils.inverter_vetor(vetor)
        elif digito == 6:
            vetor = vetor_utils.embaralhar_vetor(vetor)
    else:
        estrutura_inicial_de_sub_menu()
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()

    return vetor


#Agregada de menu_de_atualizacao_regrada - Substitui os valores negativos do vetor analisado por valores aleatórios
#dentro de um intervalo determinado de números
def substituir_negativos_aleatoriamente(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS):
    for cont in range(len(vetor)):
        if vetor[cont] < 0:
            vetor[cont] = uniform(limite_inferior, limite_superior)
            vetor[cont] = truncar_casas_decimais(vetor[cont], CASAS_DECIMAIS)

    return vetor


#Agregada de menu_atualizacao_regrada - Multiplica os valores do vetor analisado por uma fração digitada pelo usuário
#O.B.S: Não entendi bem o que era pra fazer nessa parte, então saiu essa bomba aqui
def multiplicar_por_fracao(vetor, numerador, denominador, CASAS_DECIMAIS):
    for cont in range(len(vetor)):
        vetor[cont] *= numerador / denominador
        vetor[cont] = truncar_casas_decimais(vetor[cont], CASAS_DECIMAIS)
    
    return vetor


#Menu referente à adição de novos valores no vetor analisado
def menu_de_adicao_de_novos_valores(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        quant_novos_valores = pedir_int_min('\n-> Digite quantos valores você gostaria de adicionar (mínimo 1): ', 1)
        print(f'\nLimite inferior atual: {limite_inferior:.2f}\nLimite superior atual: {limite_superior:.2f}\n')

        vetor = vetor_utils.adicionar_novos_valores_in_range(vetor, quant_novos_valores, limite_inferior, limite_superior)
        vetor = vetor_utils.truncar_casas_decimais_de_vetor(vetor, CASAS_DECIMAIS)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_NAO_INICIALIZADO)

    estrutura_final_de_sub_menu()

    return vetor


#Menu referente à remoção de um ou mais elementos do vetor pelo seu valor exato
def menu_de_remocao_por_valor(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        valor_removido = pedir_float('-> Digite o valor que será removido: ')
        vetor = vetor_utils.remover_valor_exato(vetor, valor_removido)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()

    return vetor


#Menu referente à remoção de um elemento do vetor pela sua posicao
def menu_de_remocao_por_posicao(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        posicao = pedir_int_min_max('-> Digite a posição do valor a ser removido: ', 1, len(vetor)) - 1
        vetor = vetor_utils.remover_valor_por_indice(vetor, posicao)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)
    
    estrutura_final_de_sub_menu()


#Menu referente à edição de um elemento do vetor pela sua posição
def menu_de_edicao_por_posicao(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        posicao = pedir_int_min_max('Digite a posição do valor a ser editado: ', 1, len(vetor)) - 1
        print(f'\nValor atual da posição selecionada: {vetor[posicao]}')

        vetor[posicao] = pedir_float_min_max('-> Digite o novo valor (obedecendo limites inferior e superior previamente impostos): ', limite_inferior, limite_superior)
        vetor[posicao] = truncar_casas_decimais(vetor[posicao], CASAS_DECIMAIS)
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Menu referente ao processo de salvar os valores do vetor analisado em um arquivo
def menu_de_salvar_arquivo(vetor):
    estrutura_inicial_de_sub_menu()

    if len(vetor) > 0:
        nome_do_arquivo = pedir_string('Digite o nome do arquivo onde os valores serão salvos (sem o nome do formato): ')
        vetor_utils.salvar_vetor_em_txt(vetor, nome_do_arquivo)
        print('Arquivo salvo com sucesso!')
    else:
        escrever_mensagem_de_erro(MENSAGEM_DE_VETOR_VAZIO)

    estrutura_final_de_sub_menu()


#Escreve uma mensagem de erro na tela
def escrever_mensagem_de_erro(mensagem_de_erro):
    print(mensagem_de_erro)


#Sai do programa, salvando automaticamente os valores do vetor em um arquivo
def sair_do_programa(vetor):
    if len(vetor) > 0:
        vetor_utils.salvar_vetor_em_txt(vetor, 'automatico')

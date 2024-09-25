# Arquivo que reúne as funções e textos específicos do gerenciador de montadoras


from utils.io_utils import limpar_tela, pedir_int_min_max, pedir_string, erro
from utils.vetor_utils import filtrar, mapear
from ulid import ULID
from os import path, makedirs

from patrocars_utils import (
    estrutura_basica_de_gerenciador, estrutura_inicial_de_menu, estrutura_final_de_menu, INPUT_BASICO, pedir_ulid_valido,
    retornar_valor_booleano, pedir_opcao_de_filtro_de_lista, salvar_lista_em_json, pedir_opcao_de_atributos,
    ordenar_lista_por_atributo, pedir_opcao_de_ordem_de_listagem, retornar_lista_em_ordem_desejada
    )


# Sub-menu referente aos atributos de listagem de montadoras
SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS = '''
=======================================================================================================================================
| Digite 1 para ordenar por ID
| Digite 2 para ordenar por NOME
| Digite 3 para ordenar por PAÍS
| Digite 4 para ordenar por ANO DE FUNDAÇÃO
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à operação de filtrar montadoras
SUB_MENU_DE_FILTRO_DE_MONTADORAS = '''
=======================================================================================================================================
| Digite 1 para filtrar por parte do NOME DA MONTADORA
| Digite 2 para filtrar por parte do NOME DO PAÍS DA MONTADORA
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Conjunto de mensagem de erros do gerenciador de montadoras
MENSAGEM_DE_MONTADORAS_VAZIAS = 'Não há nenhuma montadora registrada'
MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MONTADORAS = 'Não foram encontradas montadoras que correspondam à sua busca'


# Operação de atribuir uma nova montadora à lista de montadoras
def criar_nova_montadora(montadoras, nome, pais, ano_fundacao):
    montadoras.append({
        'ulid': ULID(),
        'nome': nome,
        'pais': pais,
        'ano_fundacao': ano_fundacao
    })

    return montadoras


# Operação padrão de ordenar e listar as montadoras de acordo com os parâmetros escolhidos pelo usuário.
def retornar_montadoras_ordenadas(montadoras, numero_de_atributos_de_montadoras):
    opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS, 
    numero_de_atributos_de_montadoras)

    if opcao_de_atributo != 0:
        atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
        montadoras = ordenar_lista_por_atributo(montadoras, atributo)

        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

        if opcao_de_ordem_de_listagem != 0:
            montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

            estrutura_inicial_de_menu()
            escrever_lista_de_montadoras(montadoras)
    else:
        opcao_de_ordem_de_listagem = 0

    return montadoras, opcao_de_ordem_de_listagem


# Operação de ordenar a lista de montadoras de acordo com os parâmetros escolhidos pelo usuário.
def ordenar_montadoras(montadoras, opcao_de_atributo, opcao_de_ordem_de_listagem):
    atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
    montadoras = ordenar_lista_por_atributo(montadoras, atributo)

    if opcao_de_ordem_de_listagem != 0:
        montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

    return montadoras


# Operação de escrever a lista de montadoras registradas no sistema e seus atributos
def escrever_lista_de_montadoras(montadoras):
    for montadora in montadoras:
        print(f'ULID: {montadora['ulid']} - Nome: {montadora['nome']}', end=' ')
        print(f'- País: {montadora['pais']} - Ano de fundação: {montadora['ano_fundacao']}')


# Operação de retornar o atributo de montadoras que será tomado como referência para a ordenação, de acordo com a sua 
# nomenclatura no dicionário da lista.
def retornar_atributo_de_montadoras(opcao_de_atributo):
    if opcao_de_atributo == 1:
        return 'ulid'
    elif opcao_de_atributo == 2:
        return 'nome'
    elif opcao_de_atributo == 3:
        return 'pais'

    return 'ano_fundacao'


# Operação de atualizar as informações de uma montadora
def atualizar_montadoras(montadoras, ulid_da_montadora_atualizada):
    for montadora in montadoras:
        if montadora['ulid'] == ulid_da_montadora_atualizada:
            montadora['nome'] = pedir_string('\n-> Digite o nome ATUALIZADO da montadora: ').upper()
            montadora['pais'] = pedir_string('-> Digite o nome ATUALIZADO do país da montadora: ').upper()
            montadora['ano_fundacao'] = pedir_int_min_max('-> Digite o ano ATUALIZADO de fundação da montadora: ', 1886, 2024)
            break

    return montadoras


# Remove uma montadora do sistema e todos os modelos e veículos vinculados à mesma
def remover_montadora_e_relacionados(montadoras, modelos_de_veiculos, veiculos, ulid_da_montadora_removida):
    nova_montadoras = filtrar(lambda montadora: montadora['ulid'] != ulid_da_montadora_removida, montadoras)

    ulids_dos_modelos_removidos = mapear(lambda modelo: modelo['ulid'], 
    filtrar(lambda modelo: modelo['montadora_id'] == ulid_da_montadora_removida, modelos_de_veiculos))
    
    nova_modelos_de_veiculos = filtrar(lambda modelo: modelo['ulid'] not in ulids_dos_modelos_removidos, modelos_de_veiculos)
    nova_veiculos = filtrar(lambda veiculo: veiculo['modelo_id'] not in ulids_dos_modelos_removidos, veiculos)
    
    return nova_montadoras, nova_modelos_de_veiculos, nova_veiculos


# Operação de atribuir a opção de filtro escolhida pelo usuário a uma variável
def retornar_filtro_de_montadoras(opcao_de_filtro):
    if opcao_de_filtro == 1:
        return 'nome'
    
    return 'pais'


# Operação de mostrar quantas montadoras estão cadastradas
def mostrar_status_de_montadoras(montadoras):
    if len(montadoras) > 1:
        print(f'Temos {len(montadoras)} montadoras cadastradas')
    else:
        print(f'Temos 1 montadora cadastrada')


# Processo de salvar os dados das montadoras em um arquivo .txt
def salvar_montadoras_em_txt(montadoras, nome_do_arquivo):
    if not path.exists('saves'):
        makedirs('saves')
    
    nome_do_arquivo = path.join('saves', nome_do_arquivo + '.txt')

    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in montadoras:
            linha = f"ULID: {linha['ulid']} - Nome: {linha['nome']} - País: {linha['pais']} - Ano de fundação: {linha['ano_fundacao']}\n"
            arquivo.write(linha)


# Menu referente ao gerenciamento de montadoras no sistema
def gerenciador_de_montadoras(montadoras, modelos_de_veiculos, veiculos):
    estrutura_basica_de_gerenciador('GERENCIADOR DE MONTADORAS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 6)
    nome_do_arquivo = 'montadoras'
    NUMERO_DE_ATRIBUTOS_DE_MONTADORAS = 4
    QUANT_FILTROS_DE_MONTADORAS = 2 # Quantidade de opções de filtragens disponíveis

    if opcao_de_gerenciador == 1: # Opção de criar uma nova montadora
        estrutura_inicial_de_menu()
        nome =  pedir_string('-> Digite o nome da nova montadora: ').upper()
        pais = pedir_string('-> Digite o nome do país da montadora: ').upper()
        ano_fundacao = pedir_int_min_max('-> Digite o ano de fundação da montadora: ', 1886, 2024)
        montadoras = criar_nova_montadora(montadoras, nome, pais, ano_fundacao)
        estrutura_final_de_menu()
    elif opcao_de_gerenciador == 2: # Opção de listar as montadoras registradas
        if len(montadoras) > 0:
            montadoras, opcao_de_ordem_de_listagem = retornar_montadoras_ordenadas(montadoras, NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de uma montadora
        if len(montadoras) > 0:
            montadoras, opcao_de_ordem_de_listagem = retornar_montadoras_ordenadas(montadoras, NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

            if opcao_de_ordem_de_listagem != 0:
                ulid_da_montadora_atualizada = pedir_string('\n-> Digite o ULID da montadora a ser atualizada (Copie e cole para facilitar): ')
                montadoras = atualizar_montadoras(montadoras, ulid_da_montadora_atualizada)
                estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover uma montadora do sistema
        if len(montadoras) > 0:
            montadoras, opcao_de_ordem_de_listagem = retornar_montadoras_ordenadas(montadoras, NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

            if opcao_de_ordem_de_listagem != 0:
                print('\nO.B.S: A operação de remover uma montadora também irá remover todos os modelos e veículos vinculados à mesma')
                ulid_da_montadora_removida = pedir_ulid_valido('-> Digite o ULID da montadora a ser removida (Copie e cole para facilitar): ',
                montadoras)
                confirmacao_de_remocao = retornar_valor_booleano('\n-> Você realmente quer remover essa montadora? S/N - ', 'S', 'N')

                if confirmacao_de_remocao:
                    montadoras, modelos_de_veiculos, veiculos = remover_montadora_e_relacionados(montadoras, modelos_de_veiculos,
                    veiculos, ulid_da_montadora_removida)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar as montadoras de acordo com atributos específicos
        if len(montadoras) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_lista(SUB_MENU_DE_FILTRO_DE_MONTADORAS, QUANT_FILTROS_DE_MONTADORAS)

            if opcao_de_filtro != 0:
                filtro = retornar_filtro_de_montadoras(opcao_de_filtro)
                sequencia = pedir_string('-> Digite a sequência de letras a ser filtrada: ').upper()

                # Operação de filtrar a lista de montadoras por uma sequência de letras em seu nome ou no nome de seu país
                montadoras_filtradas = filtrar(lambda montadora: sequencia in montadora[filtro], montadoras)

                if len(montadoras_filtradas) > 0:
                    montadoras_filtradas, opcao_de_ordem_de_listagem = retornar_montadoras_ordenadas(montadoras_filtradas, 
                    NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)
                    estrutura_final_de_menu()
                else:
                    estrutura_inicial_de_menu()
                    erro(MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MONTADORAS)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 6: # Opção de mostrar o número de montadoras registradas
        mensagem = lambda: mostrar_status_de_montadoras(montadoras) if len(montadoras) > 0 else erro(MENSAGEM_DE_MONTADORAS_VAZIAS)

        estrutura_inicial_de_menu()
        mensagem()
        estrutura_final_de_menu()
    else:
        limpar_tela()
        salvar_lista_em_json(montadoras, nome_do_arquivo)
        salvar_montadoras_em_txt(montadoras, nome_do_arquivo)

        return montadoras, modelos_de_veiculos, veiculos
    
    salvar_lista_em_json(montadoras, nome_do_arquivo)
    salvar_montadoras_em_txt(montadoras, nome_do_arquivo)

    return gerenciador_de_montadoras(montadoras, modelos_de_veiculos, veiculos)

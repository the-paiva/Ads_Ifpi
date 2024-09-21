# Atividade Y - Patrocars


from ulid import ULID
from utils.io_utils import limpar_tela, pedir_int_min_max, pedir_string, erro, enter_para_limpar_tela, pedir_float_min, pedir_int_min, pedir_boolean
from utils.vetor_utils import filtrar, inverter_vetor
from utils.math_utils import truncar_casas_decimais
from os import path
from json import dump, load


# Menu principal do sistema
MENU_PRINCIPAL = '''
========================================================= PATROCARS =========================================================
| Digite 1 para entrar no menu de gerenciamento de montadoras
| Digite 2 para entrar no menu de gerenciamento de modelos de veículos
| Digite 3 para entrar no menu de gerenciamento de veículos
| Digite 0 para sair do sistema
| O.B.S: Novos dados serão salvos automaticamente à medida em que forem criados
=============================================================================================================================
'''


# Sub-menu referente aos atributos de listagem de montadoras
SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS = '''
=============================================================================================================================
| Digite 1 para ordenar por NOME
| Digite 2 para ordenar por PAÍS
| Digite 3 para ordenar por ANO DE FUNDAÇÃO
| Digite 0 para voltar ao menu do gerenciador
=============================================================================================================================
'''


# Sub-menu referente aos atributos de listagem de modelos de veículos
SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS = '''
=============================================================================================================================
| Digite 1 para ordenar por ID do MODELO DO VEÍCULO
| Digite 2 para ordenar por ID da montadora
| Digite 3 para ordenar por NOME
| Digite 4 para ordenar por VALOR DE REFERÊNCIA
| Digite 5 para ordernar por MOTORIZAÇÃO
| Digite 6 para ordenar por SISTEMA DE TURBO
| Digite 7 para ordenar por CÂMBIO AUTOMÁTICO
=============================================================================================================================
'''


# Sub-menu referente à ordem de listagem (ascendente ou descendente)
SUB_MENU_DE_ORDEM_DE_LISTAGEM = '''
=============================================================================================================================
| Digite 1 para ordenar de forma ASCENDENTE
| Digite 2 para ordenar de forma DESCENDENTE
| Digite 0 para voltar ao menu do gerenciador
=============================================================================================================================
'''


# Sub-menu referente à operação de filtrar montadoras
SUB_MENU_DE_FILTRO_DE_MONTADORAS = '''
=============================================================================================================================
| Digite 1 para filtrar por parte do NOME DA MONTADORA
| Digite 2 para filtrar por parte do NOME DO PAÍS da montadora
| Digite 0 para voltar ao menu do gerenciador
=============================================================================================================================
'''


# Mensagem básica de input usada diversas vezes
INPUT_BASICO = '-> Escolha uma das opções acima: '


# Conjunto de mensagens de erros usadas no sistema
MENSAGEM_DE_MONTADORAS_VAZIAS = 'Não há nenhuma montadora registrada'
MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MONTADORAS = 'Não foram encontradas montadoras que correspondam à sua busca'
MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIA = 'Não há nenhum modelo de veículo registrado'


# Estrutura básica compartilhada pelos gerenciadores do sistema
def estrutura_basica_de_gerenciador(titulo):
    COMPRIMENTO_DO_MENU = 125
    limpar_tela()
    print(f'''
=============================================================================================================================
{titulo:^{COMPRIMENTO_DO_MENU}}
=============================================================================================================================
| 1. Criar
| 2. Listar
| 3. Atualizar
| 4. Remover
| 5. Filtrar
| 6. Status
| 0. Voltar ao menu principal
=======================================================================================================================
''')


# Estrutura que alguns dos menus do sistema contêm em seu início
def estrutura_inicial_de_menu():
    limpar_tela()
    print('=============================================================================================================================')


# Estrutura que alguns dos menus do sistema contêm em seu fim
def estrutura_final_de_menu():
    print('=============================================================================================================================')
    enter_para_limpar_tela()


# Operação de carregar os dados de algum arquivo para uma lista. Retorna uma lista vazia, caso não encontre nenhum
# arquivo válido.
def carregar_arquivo(nome_do_arquivo):
    nome_do_arquivo = nome_do_arquivo + '.json'

    if path.exists(nome_do_arquivo):
        with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
            lista = load(arquivo, object_hook=converter_string_para_ulid)
    else:
        lista = []

    return lista


# Menu referente ao gerenciamento de montadoras no sistema
def gerenciador_de_montadoras(montadoras):
    estrutura_basica_de_gerenciador('GERENCIADOR DE MONTADORAS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 6)
    nome_do_arquivo = 'montadoras'
    NUMERO_DE_ATRIBUTOS_DE_MONTADORAS = 3

    if opcao_de_gerenciador == 1: # Opção de criar uma nova montadora
        estrutura_inicial_de_menu()
        montadoras = criar_nova_montadora(montadoras)
        estrutura_final_de_menu()
    elif opcao_de_gerenciador == 2: # Opção de listar as montadoras registradas
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS, 
            NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de uma montadora
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS, 
            NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_atualizada = pedir_string('\n-> Digite o ULID da montadora a ser atualizada (Copie e cole para facilitar): ')
            montadoras = atualizar_montadoras(montadoras, ulid_da_montadora_atualizada)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover uma montadora do sistema
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS, 
            NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_removida = pedir_string('\n-> Digite o ULID da montadora a ser removida (Copie e cole para facilitar): ')
            montadoras = remover_montadora(montadoras, ulid_da_montadora_removida)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar as montadoras de acordo com atributos específicos
        if len(montadoras) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_montadoras()

            if opcao_de_filtro != 0:
                filtro = retornar_filtro(opcao_de_filtro)
                sequencia = pedir_string('-> Digite a sequência a ser filtrada: ').upper()
                montadoras_filtradas = filtrar_montadoras(montadoras, filtro, sequencia)

                if len(montadoras_filtradas) > 0:
                    opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MONTADORAS, 
                    NUMERO_DE_ATRIBUTOS_DE_MONTADORAS)

                    if opcao_de_atributo != 0:
                        atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                        montadoras_filtradas = ordenar_lista_por_atributo(montadoras_filtradas, atributo)

                        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                        if opcao_de_ordem_de_listagem != 0:
                            montadoras_filtradas = retornar_lista_em_ordem_desejada(montadoras_filtradas, opcao_de_ordem_de_listagem)

                            estrutura_inicial_de_menu()
                            escrever_lista_de_montadoras(montadoras_filtradas)
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

        return montadoras
    
    salvar_lista_em_json(montadoras, nome_do_arquivo)
    salvar_montadoras_em_txt(montadoras, nome_do_arquivo)

    return gerenciador_de_montadoras(montadoras)


# Agregada de gerenciador_de_montadoras - Operação de atribuir uma nova montadora à lista de montadoras
def criar_nova_montadora(montadoras):
    montadoras.append({
        'id': ULID(),
        'nome': pedir_string('-> Digite o nome da nova montadora: ').upper(),
        'pais': pedir_string('-> Digite o nome do país da montadora: ').upper(),
        'ano_fundacao': pedir_int_min_max('-> Digite o ano de fundação da montadora: ', 1886, 2024)
    })

    return montadoras


# Agregada de gerenciador_de_montadoras - Operação de escrever a lista de montadoras registradas no sistema e seus atributos
def escrever_lista_de_montadoras(montadoras):
    for montadora in montadoras:
        print(f'ULID: {montadora['id']} - Nome: {montadora['nome']}', end=' ')
        print(f'- País: {montadora['pais']} - Ano de fundação: {montadora['ano_fundacao']}')


# Agregada de gerenciador_de_montadoras - Operação de retornar o atributo de montadoras que será tomado como referência 
# para a ordenação, de acordo com a sua nomenclatura no dicionário da lista.
def retornar_atributo_de_montadoras(opcao_de_atributo):
    if opcao_de_atributo == 1:
        return 'nome'
    elif opcao_de_atributo == 2:
        return 'pais'

    return 'ano_fundacao'
    

# Agregada de gerenciador_de_montadoras - Operação de retornar a lista de montadoras de acordo com a sua ordem de ascendência
# (Ascendente ou descendente).
def retornar_lista_em_ordem_desejada(lista, opcao_de_ordem_de_listagem):
    if opcao_de_ordem_de_listagem == 2: # 2 é a opção correspondente à ordem descendente
        lista = inverter_vetor(lista)

    return lista


# Agregada de gerenciador_de_montadoras - Operação de atualizar as informações de uma montadora
def atualizar_montadoras(montadoras, ulid_da_montadora_atualizada):
    for montadora in montadoras:
        if montadora['id'] == ulid_da_montadora_atualizada:
            montadora['nome'] = pedir_string('\n-> Digite o nome ATUALIZADO da nova montadora: ').upper()
            montadora['pais'] = pedir_string('-> Digite o nome ATUALIZADO do país da montadora: ').upper()
            montadora['ano_fundacao'] = pedir_int_min_max('-> Digite o ano ATUALIZADO de fundação da montadora: ', 1886, 2024)
            break

    return montadoras


# Agregada de gerenciador_de_montadoras - Operação de remover uma montadora do sistema
def remover_montadora(montadoras, ulid_da_montadora_removida):
    return filtrar(lambda montadora: montadora['id'] != ulid_da_montadora_removida, montadoras)


# Agregada de gerenciador_de_montadoras - Operação de filtrar a lista de montadoras com base em parâmetros específicos
def filtrar_montadoras(montadoras, filtro, sequencia):
    montadoras_filtradas = []

    for montadora in montadoras:
        if sequencia in montadora[filtro].upper():
            montadoras_filtradas.append(montadora)

    return montadoras_filtradas


# Agregada de gerenciador_de_montadoras - Operação de pedir que o usuário escolha uma das opções de filtragem apresentadas
def pedir_opcao_de_filtro_de_montadoras():
    limpar_tela()
    print(SUB_MENU_DE_FILTRO_DE_MONTADORAS)
    opcao_de_filtro = pedir_int_min_max(INPUT_BASICO, 0, 2)

    return opcao_de_filtro


# Agregada de gerenciador_de_montadoras - Operação de atribuir a opção de filtro escolhida pelo usuário a uma variável
def retornar_filtro(opcao_de_filtro):
    if opcao_de_filtro == 1:
        return 'nome'
    
    return 'pais'


# Agregada de gerenciador_de_montadoras - Operação de mostrar quantas montadoras estão cadastradas
def mostrar_status_de_montadoras(montadoras):
    if len(montadoras) > 1:
        print(f'Temos {len(montadoras)} montadoras cadastradas')
    else:
        print(f'Temos 1 montadora cadastrada')


# Menu referente ao gerenciamento de modelos de veículos no sistema
def gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras):
    estrutura_basica_de_gerenciador('GERENCIADOR DE MODELOS DE VEÍCULOS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 6)
    nome_do_arquivo = 'modelos_de_veiculos'
    NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS = 7
    CASAS_DECIMAIS = 2 # Casas decimais para valores float - EX: Valor de referência

    if opcao_de_gerenciador == 1: # Opção de registrar um novo modelo de veículo no sistema
        estrutura_inicial_de_menu()
        escrever_lista_de_montadoras(montadoras)
        montadora_id = pedir_string('\n-> Escolha uma das montadoras listadas pelo ULID (Copie e cole para facilitar): ')

        estrutura_inicial_de_menu()
        ulid = ULID()
        nome = pedir_string('-> Digite o nome do modelo de veículo: ')
        valor_referencia = pedir_float_min('-> Digite um valor de referência para o modelo: ', 1000)
        motorizacao = pedir_int_min('-> Digite a motorização do veículo (em cavalos de potência): ', 1)
        turbo = pedir_boolean('O carro possui sistema de turbo? S/N: ', 'S', 'N').upper()
        automatico = pedir_boolean('O carro possui câmbio automático? S/N: ', 'S', 'N').upper()

        valor_referencia = truncar_casas_decimais(valor_referencia, CASAS_DECIMAIS)

        modelos_de_veiculos = criar_modelo_de_veiculo(modelos_de_veiculos, ulid, montadora_id, nome, valor_referencia, 
        motorizacao, turbo, automatico)

        estrutura_final_de_menu()
    if opcao_de_gerenciador == 2: # Opção de listar os modelos de veículos já registrados
        if len(modelos_de_veiculos) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS, 
            NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS)

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_modelos_de_veiculos(opcao_de_atributo)
                modelos_de_veiculos = ordenar_lista_por_atributo(modelos_de_veiculos, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    modelos_de_veiculos = retornar_lista_em_ordem_desejada(modelos_de_veiculos, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIA)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de um modelo de veículo
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos()

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_atualizada = pedir_string('\n-> Digite o ULID da montadora a ser atualizada (Copie e cole para facilitar): ')
            montadoras = atualizar_montadoras(montadoras, ulid_da_montadora_atualizada)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover uma modelo de veículo do sistema
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos()

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_removida = pedir_string('\n-> Digite o ULID da montadora a ser removida (Copie e cole para facilitar): ')
            montadoras = remover_montadora(montadoras, ulid_da_montadora_removida)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar os modelos de veículos de acordo com atributos específicos
        if len(montadoras) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_montadoras()

            if opcao_de_filtro != 0:
                filtro = retornar_filtro(opcao_de_filtro)
                sequencia = pedir_string('-> Digite a sequência a ser filtrada: ').upper()
                montadoras_filtradas = filtrar_montadoras(montadoras, filtro, sequencia)

                if len(montadoras_filtradas) > 0:
                    opcao_de_atributo = pedir_opcao_de_atributos()

                    if opcao_de_atributo != 0:
                        atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                        montadoras_filtradas = ordenar_lista_por_atributo(montadoras_filtradas, atributo)

                        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                        if opcao_de_ordem_de_listagem != 0:
                            montadoras_filtradas = retornar_lista_em_ordem_desejada(montadoras_filtradas, opcao_de_ordem_de_listagem)

                            estrutura_inicial_de_menu()
                            escrever_lista_de_montadoras(montadoras_filtradas)
                            estrutura_final_de_menu()
                else:
                    estrutura_inicial_de_menu()
                    erro(MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MONTADORAS)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 6: # Opção de mostrar o número de modelos de veículos registradas
        mensagem = lambda: mostrar_status_de_montadoras(montadoras) if len(montadoras) > 0 else erro(MENSAGEM_DE_MONTADORAS_VAZIAS)

        estrutura_inicial_de_menu()
        mensagem()
        estrutura_final_de_menu()
    else:
        limpar_tela()
        salvar_lista_em_json(modelos_de_veiculos, nome_do_arquivo)
        salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo)

        return modelos_de_veiculos
    
    salvar_lista_em_json(modelos_de_veiculos, nome_do_arquivo)
    salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo)

    return gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras)


# Agregada de gerenciador_de_modelos_de_veiculos - Operação de atribuir um novo modelo de veículo à lista dos modelos de veículos
def criar_modelo_de_veiculo(modelos_de_veiculos, ulid, montadora_id, nome, valor_referencia, motorizacao, turbo, automatico):
    modelos_de_veiculos.append({
        'id': ulid,
        'montadora_id': montadora_id,
        'nome': nome,
        'valor_referencia': valor_referencia,
        'motorizacao': motorizacao,
        'turbo': turbo,
        'automatico': automatico
    })

    return modelos_de_veiculos


# Agregada de gerenciador_de_modelos_de_veiculos - Operação de listar os modelos de veículos registrados e seus atributos
def escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos):
    for modelo in modelos_de_veiculos:
        print(f'ULID: {modelo['id']} - ID da montadora: {modelo['montadora_id']} - Nome: {modelo['nome']}')
        print(f'- Valor de referência: R$ {modelo['valor_referencia']} - Motorização: {modelo['motorizacao']} HP', end=' ')
        print(f'- Turbo: {modelo['turbo']} - Automático: {modelo['automatico']}\n')


# Agregada de gerenciador_de_modelos_de_veiculos - Operação de retornar o atributo de modelos de veículos que será tomado 
# como referência para a ordenação, de acordo com a sua nomenclatura no dicionário da lista.
def retornar_atributo_de_modelos_de_veiculos(opcao_de_atributo):
    if opcao_de_atributo == 1:
        return 'id'
    elif opcao_de_atributo == 2:
        return 'montadora_id'
    elif opcao_de_atributo == 3:
        return 'nome'
    elif opcao_de_atributo == 4:
        return 'valor_referencia'
    elif opcao_de_atributo == 5:
        return 'motorizacao'
    elif opcao_de_atributo == 6:
        return 'turbo'
    
    return 'automatico'


# Agregada de gerenciador_de_modelos_de_veiculos - Operação de salvar os dados de modelos de veículos em arquivo .txt
def salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo):
    if len(modelos_de_veiculos) > 0:
        nome_do_arquivo += '.txt'
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in modelos_de_veiculos:
                linha = (
                    f"ULID: {linha['id']} - ID da montadora: {linha['montadora_id']} - Nome: {linha['nome']}\n"
                    f"Valor de referência: R$ {linha['valor_referencia']} - Motorização: {linha['motorizacao']} "
                    f"Turbo: {linha['turbo']} - Automático: {linha['automatico']}\n\n"
                )
                arquivo.write(linha)


# Menu referente ao gerenciamento de veículos no sistema
def gerenciador_de_veiculos(veiculos):
    estrutura_basica_de_gerenciador('GERENCIADOR DE VEÍCULOS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 6)
    nome_do_arquivo = 'montadoras'

    if opcao_de_gerenciador == 1: # Opção de criar uma nova montadora
        estrutura_inicial_de_menu()
        montadoras = criar_nova_montadora(montadoras)
        estrutura_final_de_menu()
    elif opcao_de_gerenciador == 2: # Opção de listar as montadoras registradas
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos()

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de uma montadora
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos()

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_atualizada = pedir_string('\n-> Digite o ULID da montadora a ser atualizada (Copie e cole para facilitar): ')
            montadoras = atualizar_montadoras(montadoras, ulid_da_montadora_atualizada)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover uma montadora do sistema
        if len(montadoras) > 0:
            opcao_de_atributo = pedir_opcao_de_atributos()

            if opcao_de_atributo != 0:
                atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                montadoras = ordenar_lista_por_atributo(montadoras, atributo)

                opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                if opcao_de_ordem_de_listagem != 0:
                    montadoras = retornar_lista_em_ordem_desejada(montadoras, opcao_de_ordem_de_listagem)

                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

            ulid_da_montadora_removida = pedir_string('\n-> Digite o ULID da montadora a ser removida (Copie e cole para facilitar): ')
            montadoras = remover_montadora(montadoras, ulid_da_montadora_removida)
            estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MONTADORAS_VAZIAS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar as montadoras de acordo com atributos específicos
        if len(montadoras) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_montadoras()

            if opcao_de_filtro != 0:
                filtro = retornar_filtro(opcao_de_filtro)
                sequencia = pedir_string('-> Digite a sequência a ser filtrada: ').upper()
                montadoras_filtradas = filtrar_montadoras(montadoras, filtro, sequencia)

                if len(montadoras_filtradas) > 0:
                    opcao_de_atributo = pedir_opcao_de_atributos()

                    if opcao_de_atributo != 0:
                        atributo = retornar_atributo_de_montadoras(opcao_de_atributo)
                        montadoras_filtradas = ordenar_lista_por_atributo(montadoras_filtradas, atributo)

                        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

                        if opcao_de_ordem_de_listagem != 0:
                            montadoras_filtradas = retornar_lista_em_ordem_desejada(montadoras_filtradas, opcao_de_ordem_de_listagem)

                            estrutura_inicial_de_menu()
                            escrever_lista_de_montadoras(montadoras_filtradas)
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

        return montadoras
    
    salvar_lista_em_json(montadoras, nome_do_arquivo)
    salvar_montadoras_em_txt(montadoras, nome_do_arquivo)

    return gerenciador_de_montadoras(montadoras)


# Ordena os elementos de uma lista de acordo com um atributo
def ordenar_lista_por_atributo(lista, atributo):
    tamanho_da_lista = len(lista)

    for i in range(tamanho_da_lista):
        for j in range(0, tamanho_da_lista - i - 1):
            if lista[j][atributo] > lista[j+1][atributo]:
                valor_temporario = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = valor_temporario
    
    return lista


# Pede o atributo que será considerado durante a exibição dos elementos de uma lista
def pedir_opcao_de_atributos(sub_menu_de_atributos, numero_de_atributos):
    limpar_tela()
    print(sub_menu_de_atributos)
    opcao_de_atributo = pedir_int_min_max(INPUT_BASICO, 0, numero_de_atributos)
    limpar_tela()

    return opcao_de_atributo


# Pede a ordem na qual os elementos de uma lista serão exibidos
def pedir_opcao_de_ordem_de_listagem():
    limpar_tela()
    print(SUB_MENU_DE_ORDEM_DE_LISTAGEM)
    opcao_de_ordem_de_listagem = pedir_int_min_max(INPUT_BASICO, 0, 2)
    limpar_tela()

    return opcao_de_ordem_de_listagem


# Processo de salvar os dados de uma lista em um arquivo .json
def salvar_lista_em_json(lista, nome_do_arquivo):
    if len(lista) > 0:
        nome_do_arquivo = nome_do_arquivo + '.json'
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            dump(lista, arquivo, ensure_ascii=False, indent=4, default=converter_ulid_para_string)


# Agregada de gerenciador_de_montadoras - Processo de salvar os dados das montadoras em um arquivo .txt
def salvar_montadoras_em_txt(montadoras, nome_do_arquivo):
    if len(montadoras) > 0:
        nome_do_arquivo += '.txt'
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in montadoras:
                linha = f"ULID: {linha['id']} - Nome: {linha['nome']} - País: {linha['pais']} - Ano de fundação: {linha['ano_fundacao']}\n"
                arquivo.write(linha)

    
# Processo de converter uma chave ULID para string, permitindo assim que um ID seja manipulado pelos métodos JSON
def converter_ulid_para_string(id):
    if type(id) == ULID:
        return str(id)
    

# Processo de converter uma string de ULID de volta para o objeto ULID
def converter_string_para_ulid(lista):
    if type(lista['id']) == str:
        try:
           lista['id'] = ULID(lista['id']) 
        except ValueError:
            pass
    
    return lista


def main():
    montadoras = carregar_arquivo('montadoras')
    modelos_de_veiculos = carregar_arquivo('modelos_de_veiculos')
    veiculos = carregar_arquivo('veiculos')
    opcao_principal = -1

    while opcao_principal != 0: # Fluxo principal do sistema
        print(MENU_PRINCIPAL)
        opcao_principal = pedir_int_min_max('-> Digite uma das opções acima: ', 0, 3)

        if opcao_principal == 1: # Menu de gerenciamento de montadoras
            montadoras = gerenciador_de_montadoras(montadoras)
        elif opcao_principal == 2: # Menu de gerenciamento de modelos de veículos
            modelos_de_veiculos = gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras)
        elif opcao_principal == 3: # Menu de gerenciamento de veículos
            veiculos = gerenciador_de_veiculos(veiculos)


main()

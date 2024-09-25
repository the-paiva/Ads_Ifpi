# Arquivo que reúne as funções e textos específicos do gerenciador de modelos de veículos


from utils.io_utils import limpar_tela, pedir_int_min_max, pedir_string, erro, pedir_float_min, pedir_int_min
from utils.vetor_utils import filtrar
from utils.math_utils import truncar_casas_decimais
from ulid import ULID
from os import path, makedirs
from gerenciador_de_montadoras import escrever_lista_de_montadoras

from patrocars_utils import (
    estrutura_basica_de_gerenciador, estrutura_inicial_de_menu, estrutura_final_de_menu, INPUT_BASICO, pedir_ulid_valido,
    retornar_valor_booleano, pedir_opcao_de_filtro_de_lista, salvar_lista_em_json, pedir_opcao_de_atributos,
    ordenar_lista_por_atributo, pedir_opcao_de_ordem_de_listagem, retornar_lista_em_ordem_desejada, remover_item_de_lista
    )


# Sub-menu referente aos atributos de listagem de modelos de veículos
SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS = '''
=======================================================================================================================================
| Digite 1 para ordenar por ID DO MODELO DO VEÍCULO
| Digite 2 para ordenar por ID DA MONTADORA
| Digite 3 para ordenar por NOME
| Digite 4 para ordenar por VALOR DE REFERÊNCIA
| Digite 5 para ordernar por MOTORIZAÇÃO
| Digite 6 para ordenar por SISTEMA DE TURBO
| Digite 7 para ordenar por CÂMBIO AUTOMÁTICO
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à operação de filtrar modelos de veículos
SUB_MENU_DE_FILTRO_DE_MODELOS_DE_VEICULOS = '''
=======================================================================================================================================
| Digite 1 para filtrar por parte do NOME DO MODELO DE VEÍCULO
| Digite 2 para filtrar por CÂMBIO
| Digite 3 para filtrar por MOTORIZAÇÃO
| Digite 4 para filtrar por parte do NOME DA MONTADORA
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à filtragem de modelos de veículos por seu sistema de câmbio
SUB_MENU_DE_CAMBIO = '''
=======================================================================================================================================
| Digite 1 para câmbio AUTOMÁTICO
| Digite 2 para câmbio MANUAL
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à filtragem de modelos de veículos por motorização (em cavalos de potência)
SUB_MENU_DE_MOTORIZACAO = '''
=======================================================================================================================================
| Digite 1 para filtrar por modelos que tenham EXATAMENTE o número de HP escolhido
| Digite 2 para filtrar por modelos que tenham um número de HP MAIOR do que o escolhido
| Digite 3 para filtrar por modelos que tenham um número de HP MENOR do que o escolhido
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Conjunto de mensagens de erro do gerenciador de modelos de veículos
MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS = 'Não há nenhum modelo de veículo registrado'
MENSAGEM_DE_NAO_CRIACAO_DE_NOVO_MODELO = 'Não é possível registrar um novo modelo de veículo, pois não há nenhuma montadora registrada'
MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MODELOS = 'Não foram encontrados modelos de veículos que correspondam à sua busca'


# Operação de atribuir um novo modelo de veículo à lista dos modelos de veículos
def criar_modelo_de_veiculo(modelos_de_veiculos, montadora_id, nome, valor_referencia, motorizacao, turbo, automatico):
    modelos_de_veiculos.append({
        'ulid': ULID(),
        'montadora_id': montadora_id,
        'nome': nome,
        'valor_referencia': valor_referencia,
        'motorizacao': motorizacao,
        'turbo': turbo,
        'automatico': automatico
    })

    return modelos_de_veiculos


# Operação padrão de ordenar e listar os modelos de veículos de acordo com os parâmetros escolhidos pelo usuário.
def retornar_modelos_ordenados(modelos_de_veiculos, numero_de_atributos_de_modelos_de_veiculos):
    opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS, 
    numero_de_atributos_de_modelos_de_veiculos)

    if opcao_de_atributo != 0:
        atributo = retornar_atributo_de_modelos_de_veiculos(opcao_de_atributo)
        modelos_de_veiculos = ordenar_lista_por_atributo(modelos_de_veiculos, atributo)

        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

        if opcao_de_ordem_de_listagem != 0:
            modelos_de_veiculos = retornar_lista_em_ordem_desejada(modelos_de_veiculos, opcao_de_ordem_de_listagem)

            estrutura_inicial_de_menu()
            escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos)
    else:
        opcao_de_ordem_de_listagem = 0

    return modelos_de_veiculos, opcao_de_ordem_de_listagem


# Operação de listar os modelos de veículos registrados e seus atributos
def escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos):
    for modelo in modelos_de_veiculos:
        print(f"ULID: {modelo['ulid']} - ID da montadora: {modelo['montadora_id']} - Nome: {modelo['nome']}")
        print(f"- Valor de referência: R$ {modelo['valor_referencia']} - Motorização: {modelo['motorizacao']} HP", end=' ')
        print(f"- Turbo: {modelo['turbo']} - Automático: {modelo['automatico']}\n")


# Operação de retornar o atributo de modelos de veículos que será tomado como referência para a ordenação, de acordo com a 
# sua nomenclatura no dicionário da lista.
def retornar_atributo_de_modelos_de_veiculos(opcao_de_atributo):
    if opcao_de_atributo == 1:
        return 'ulid'
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


# Operação de atualizar as informações de um modelo de veículo
def atualizar_modelo_de_veiculo(modelos_de_veiculos, ulid_do_modelo_atualizado):
    for modelo in modelos_de_veiculos:
        if modelo['ulid'] == ulid_do_modelo_atualizado:
            modelo['nome'] = pedir_string('\n-> Digite o nome ATUALIZADO do modelo: ').upper()
            modelo['valor_referencia'] = pedir_float_min('-> Digite o valor de referência ATUALIZADO do modelo: R$ ', 1000)
            modelo['motorizacao'] = pedir_int_min('-> Digite a motorização do veículo (em cavalos de potência): ', 1)
            modelo['turbo'] = retornar_valor_booleano('-> O carro possui sistema de turbo? S/N: ', 'S', 'N')
            modelo['automatico'] = retornar_valor_booleano('-> O carro possui câmbio automático? S/N: ', 'S', 'N')
            break

    return modelos_de_veiculos


# Operação de remover veículos vinculados a um modelo
def remover_veiculos_vinculados_a_modelo(veiculos, ulid_do_modelo_removido):
    return filtrar(lambda veiculo: veiculo['modelo_id'] != ulid_do_modelo_removido, veiculos)


# Operação de atribuir a opção de filtro escolhida pelo usuário à lista dos modelos de veículos.
def retornar_filtro_de_modelos_de_veiculos(opcao_de_filtro):
    if opcao_de_filtro == 1:
        return 'nome'
    elif opcao_de_filtro == 2:
        return 'automatico'
    elif opcao_de_filtro == 3:
        return 'motorizacao'
    
    return 'montadora_id'


# Operação de filtrar os modelos de veículos de acordo com uma sequência de letras no nome de sua montadora.
def filtrar_modelo_por_nome_da_montadora(modelos_de_veiculos, montadoras, sequencia):
    modelos_filtrados = []

    for montadora in montadoras:
        if sequencia in montadora['nome'].upper():
            for modelo in modelos_de_veiculos:
                if modelo['montadora_id'] == montadora['ulid']:
                    modelos_filtrados.append(modelo)

    return modelos_filtrados


# Operação de mostrar quantos modelos de veículos estão cadastrados
def mostrar_status_de_modelos_de_veiculos(modelos_de_veiculos):
    if len(modelos_de_veiculos) > 1:
        print(f'Temos {len(modelos_de_veiculos)} modelos de veículos cadastrados')
    else:
        print(f'Temos 1 modelo de veículo cadastrado')


# Operação de salvar os dados de modelos de veículos em arquivo .txt
def salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo):
    if not path.exists('saves'):
        makedirs('saves')
    
    nome_do_arquivo = path.join('saves', nome_do_arquivo + '.txt')

    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in modelos_de_veiculos:
            linha = (
                f"ULID: {linha['ulid']} - ID da montadora: {linha['montadora_id']} - Nome: {linha['nome']}\n"
                f"Valor de referência: R$ {linha['valor_referencia']} - Motorização: {linha['motorizacao']} "
                f"Turbo: {linha['turbo']} - Automático: {linha['automatico']}\n\n"
            )
            arquivo.write(linha)


# Menu referente ao gerenciamento de modelos de veículos no sistema
def gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos):
    estrutura_basica_de_gerenciador('GERENCIADOR DE MODELOS DE VEÍCULOS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 6)
    nome_do_arquivo = 'modelos_de_veiculos'
    NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS = 7
    CASAS_DECIMAIS = 2 # Casas decimais para valores float - EX: Valor de referência
    QUANT_FILTROS_DE_MODELOS = 4

    if opcao_de_gerenciador == 1: # Opção de registrar um novo modelo de veículo no sistema
        estrutura_inicial_de_menu()

        if len(montadoras) > 0:
            escrever_lista_de_montadoras(montadoras)
            montadora_id = pedir_ulid_valido('\n-> Escolha uma das montadoras listadas pelo ULID (copie e cole para facilitar): ', 
            montadoras)

            estrutura_inicial_de_menu()
            nome = pedir_string('-> Digite o nome do modelo de veículo: ').upper()
            valor_referencia = pedir_float_min('-> Digite um valor de referência para o modelo: R$ ', 1000)
            motorizacao = pedir_int_min('-> Digite a motorização do veículo (em cavalos de potência): ', 1)
            turbo = retornar_valor_booleano('-> O carro possui sistema de turbo? S/N: ', 'S', 'N')
            automatico = retornar_valor_booleano('-> O carro possui câmbio automático? S/N: ', 'S', 'N')

            valor_referencia = truncar_casas_decimais(valor_referencia, CASAS_DECIMAIS)

            modelos_de_veiculos = criar_modelo_de_veiculo(modelos_de_veiculos, montadora_id, nome, valor_referencia, 
            motorizacao, turbo, automatico)
        else:
            erro(MENSAGEM_DE_NAO_CRIACAO_DE_NOVO_MODELO)

        estrutura_final_de_menu()
        return gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos)
    if opcao_de_gerenciador == 2: # Opção de listar os modelos de veículos já registrados
        if len(modelos_de_veiculos) > 0:
            modelos_de_veiculos, opcao_de_ordem_de_listagem = retornar_modelos_ordenados(modelos_de_veiculos, 
            NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de um modelo de veículo
        if len(modelos_de_veiculos) > 0:
            modelos_de_veiculos, opcao_de_ordem_de_listagem = retornar_modelos_ordenados(modelos_de_veiculos, 
            NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                ulid_do_modelo_atualizado = pedir_ulid_valido('\n-> Digite o ULID do modelo a ser atualizado (Copie e cole para facilitar): ',
                modelos_de_veiculos)
                modelos_de_veiculos = atualizar_modelo_de_veiculo(modelos_de_veiculos, ulid_do_modelo_atualizado)
                estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover um modelo de veículo do sistema
        if len(modelos_de_veiculos) > 0:
            modelos_de_veiculos, opcao_de_ordem_de_listagem = retornar_modelos_ordenados(modelos_de_veiculos, 
            NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                print('\nO.B.S: A operação de remover um modelo também irá remover todos os veículos vinculados ao mesmo')
                ulid_do_modelo_removido = pedir_ulid_valido('-> Digite o ULID do modelo a ser removido (Copie e cole para facilitar): ',
                modelos_de_veiculos)
                confirmacao_de_remocao = retornar_valor_booleano('\n-> Você realmente quer remover esse modelo? S/N - ', 'S', 'N')

                if confirmacao_de_remocao:
                    veiculos = remover_veiculos_vinculados_a_modelo(veiculos, ulid_do_modelo_removido)
                    modelos_de_veiculos = remover_item_de_lista(modelos_de_veiculos, ulid_do_modelo_removido)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar os modelos de veículos de acordo com atributos específicos
        if len(modelos_de_veiculos) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_lista(SUB_MENU_DE_FILTRO_DE_MODELOS_DE_VEICULOS, QUANT_FILTROS_DE_MODELOS)

            if opcao_de_filtro != 0:
                filtro = retornar_filtro_de_modelos_de_veiculos(opcao_de_filtro)

                if filtro == 'nome':
                    # Filtragem pela sequência de letras no nome do modelo de veículo
                    sequencia = pedir_string('-> Digite a sequência de letras a ser filtrada: ').upper()
                    modelos_filtrados = filtrar(lambda modelo: sequencia in modelo['nome'].upper(), modelos_de_veiculos)
                elif filtro == 'automatico':
                    # Filtragem por câmbio automático
                    limpar_tela()
                    print(SUB_MENU_DE_CAMBIO)
                    opcao_de_cambio = pedir_int_min_max(INPUT_BASICO, 0, 2)

                    if opcao_de_cambio == 1:
                        modelos_filtrados = filtrar(lambda modelo: modelo['automatico'], modelos_de_veiculos)
                    elif opcao_de_cambio == 2:
                        modelos_filtrados = filtrar(lambda modelo: not modelo['automatico'], modelos_de_veiculos)
                    else:
                        return gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos)
                elif filtro == 'motorizacao':
                    # Filtragem por motorização
                    motorizacao_a_filtrar = pedir_int_min('\n-> Digite uma quantidade de HP (Cavalos de potência) a ser filtrada: ', 1)

                    limpar_tela()
                    print(SUB_MENU_DE_MOTORIZACAO)
                    opcao_de_motorizacao = pedir_int_min_max(INPUT_BASICO, 0, 3)

                    if opcao_de_motorizacao == 1:
                        # Filtrar por HP exato
                        modelos_filtrados = filtrar(lambda modelo: modelo['motorizacao'] == motorizacao_a_filtrar, 
                        modelos_de_veiculos)
                    elif opcao_de_motorizacao == 2:
                        # Filtrar por valores acima do HP escolhido
                        modelos_filtrados = filtrar(lambda modelo: modelo['motorizacao'] > motorizacao_a_filtrar,
                        modelos_de_veiculos)
                    elif opcao_de_motorizacao == 3:
                        # Filtrar por valores abaixo do HP escolhido
                        modelos_filtrados = filtrar(lambda modelo: modelo['motorizacao'] < motorizacao_a_filtrar,
                        modelos_de_veiculos)
                    else:
                        return gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos)
                else:
                    # Filtragem por sequência de letras no nome da montadora do modelo
                    sequencia = pedir_string('\n-> Digite a sequência de letras a ser filtrada: ').upper()
                    modelos_filtrados = filtrar_modelo_por_nome_da_montadora(modelos_de_veiculos, montadoras, sequencia)

                if len(modelos_filtrados) > 0:
                    modelos_filtrados, opcao_de_ordem_de_listagem = retornar_modelos_ordenados(modelos_filtrados, 
                    NUMERO_DE_ATRIBUTOS_DE_MODELOS_DE_VEICULOS)

                    if opcao_de_ordem_de_listagem != 0:
                        estrutura_final_de_menu()
                else:
                    estrutura_inicial_de_menu()
                    erro(MENSAGEM_DE_FILTRAGEM_VAZIA_DE_MODELOS)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 6: # Opção de mostrar o número de modelos de veículos registradas
        mensagem = (lambda: mostrar_status_de_modelos_de_veiculos(modelos_de_veiculos) if len(modelos_de_veiculos) > 0 
        else erro(MENSAGEM_DE_MODELOS_DE_VEICULOS_VAZIOS))

        estrutura_inicial_de_menu()
        mensagem()
        estrutura_final_de_menu()
    else:
        limpar_tela()
        salvar_lista_em_json(modelos_de_veiculos, nome_do_arquivo)
        salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo)

        return modelos_de_veiculos, veiculos
    
    salvar_lista_em_json(modelos_de_veiculos, nome_do_arquivo)
    salvar_modelos_de_veiculos_em_txt(modelos_de_veiculos, nome_do_arquivo)

    return gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos)

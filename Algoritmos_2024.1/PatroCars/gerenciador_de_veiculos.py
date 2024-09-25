# Arquivo que reúne as funções e textos específicos do gerenciador de veículos


from utils.io_utils import limpar_tela, pedir_int_min_max, pedir_string, erro, pedir_float_min
from utils.vetor_utils import filtrar
from utils.math_utils import truncar_casas_decimais
from ulid import ULID
from os import path, makedirs
from gerenciador_de_modelos_de_veiculos import escrever_lista_de_modelos_de_veiculos
from gerenciador_de_montadoras import escrever_lista_de_montadoras

from patrocars_utils import (
    estrutura_inicial_de_menu, estrutura_final_de_menu, INPUT_BASICO, pedir_ulid_valido, remover_item_de_lista,
    retornar_valor_booleano, pedir_opcao_de_filtro_de_lista, salvar_lista_em_json, pedir_opcao_de_atributos,
    ordenar_lista_por_atributo, pedir_opcao_de_ordem_de_listagem, retornar_lista_em_ordem_desejada
    )


# Sub-menu referente aos atributos de listagem de veículos
SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_VEICULOS = '''
=======================================================================================================================================
| Digite 1 para ordenar por ID DO VEÍCULO
| Digite 2 para ordenar por ID DO MODELO DO VEÍCULO
| Digite 3 para ordenar por nome da COR do veículo
| Digite 4 para ordenar por ANO DE FABRICAÇÃO DO VEÍCULO
| Digite 5 para ordenar por ANO DE FABRICAÇÃO DO MODELO DO VEÍCULO
| Digite 6 para ordenar por VALOR do veículo
| Digite 7 para ordenar por PLACA do veículo
| Digite 8 para ordenar por VENDA de veículo
| Digite 0 para voltar ao menu do gerenciador 
=======================================================================================================================================
'''

# Sub-menu referente à operação de filtrar veículos
SUB_MENU_DE_FILTRO_DE_VEICULOS = '''
=======================================================================================================================================
| Digite 1 para filtrar por PARTE DA COR
| Digite 2 para filtrar pelo ANO DE FABRICAÇÃO DO VEÍCULO
| Digite 3 para filtrar pelo ANO DE FABRICAÇÃO DO MODELO DO VEÍCULO
| Digite 4 para filtrar pelo VALOR do veículo
| Digite 5 para filtrar por veículo VENDIDO
| Digite 6 para filtrar por veículo NÃO VENDIDO
| Digite 7 para filtrar por PARTE DO NOME DA MONTADORA
| Digite 8 para filtrar por PARTE DO NOME DO MODELO DE VEÍCULO
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à filtragem de veículos por ano de fabricação ou do seu modelo ou do veículo em si
SUB_MENU_DE_ANO_A_FILTRAR = '''
=======================================================================================================================================
| Digite 1 para filtrar por ano EXATAMENTE IGUAL ao escolhido
| Digite 2 para filtrar por ano MAIOR do que o escolhido
| Digite 3 para filtrar por ano MENOR do que o escolhido
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Sub-menu referente à filtragem de veículos pelo valor
SUB_MENU_DE_VALOR_A_FILTRAR = '''
=======================================================================================================================================
| Digite 1 para filtrar por valor EXATAMENTE IGUAL ao escolhido
| Digite 2 para filtrar por valor MAIOR do que o escolhido
| Digite 3 para filtrar por valor MENOR do que o escolhido
| Digite 0 para voltar ao menu do gerenciador 
=======================================================================================================================================
'''

# Sub-menu referente à busca personalizada de veículos para venda
SUB_MENU_DE_BUSCA_PARA_VENDA = '''
=======================================================================================================================================
| Digite 1 para buscar veículos apenas de uma montadora
| Digite 2 para buscar veículos apenas de um modelo
| Digite 3 para buscar todos os veículos
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Conjunto de mensagens de erros do gerenciador de veículos
MENSAGEM_DE_VEICULOS_VAZIOS = 'Não há nenhum veículo registrado'
MENSAGEM_DE_NAO_CRIACAO_DE_NOVO_VEICULO = 'Não é possível registrar um novo veículo, pois não há nenhum modelo de veículo registrado'
MENSAGEM_DE_INDISPONIBILIDADE_DE_VEICULOS = 'No momento, não temos nenhum veículo à venda'
MENSAGEM_DE_INDISPONIBILIDADE_DE_VEICULOS_ESPECIFICOS = 'No momento, não temos nenhum veículo com os requisitos desejados à venda'
MENSAGEM_DE_FILTRAGEM_VAZIA_DE_VEICULOS = 'Não foram encontrados veículos que correspondam à sua busca'


# Estrutura específica de gerenciador de veículos
def estrutura_de_gerenciador_de_veiculos(titulo):
    COMPRIMENTO_DO_MENU = 135
    limpar_tela()
    print(f'''
=======================================================================================================================================
{titulo:^{COMPRIMENTO_DO_MENU}}
=======================================================================================================================================
| 1. Criar
| 2. Listar
| 3. Atualizar
| 4. Remover
| 5. Filtrar
| 6. Status
| 7. Vender veículo
| 0. Voltar ao menu principal
=======================================================================================================================================
''')


# Operação de atribuir um novo veículo à lista de veículos
def criar_veiculo(veiculos, modelo_id, cor, ano_fabricacao, ano_modelo, valor, placa):
    veiculos.append({
        'ulid': ULID(),
        'modelo_id': modelo_id,
        'cor': cor,
        'ano_fabricacao': ano_fabricacao,
        'ano_modelo': ano_modelo,
        'valor': valor,
        'placa': placa,
        'vendido': False
    })

    return veiculos


# Operação de listar os veículos registrados e seus atributos
def escrever_lista_de_veiculos(veiculos):
    for veiculo in veiculos:
        print(f"ULID: {veiculo['ulid']} - ID do modelo: {veiculo['modelo_id']}")
        print(f"- Cor: {veiculo['cor']} - Ano de fabricação: {veiculo['ano_fabricacao']} - Ano do modelo: {veiculo['ano_modelo']}", end=' ')
        print(f"- Valor: R$ {veiculo['valor']} - Placa: {veiculo['placa']} - Vendido: {veiculo['vendido']}\n")


# Operação padrão de ordenar e listar os veículos de acordo com os parâmetros escolhidos pelo usuário.
def retornar_veiculos_ordenados(veiculos, numero_de_atributos_de_veiculos):
    opcao_de_atributo = pedir_opcao_de_atributos(SUB_MENU_DE_ORDEM_DE_ATRIBUTOS_DE_VEICULOS, 
    numero_de_atributos_de_veiculos)

    if opcao_de_atributo != 0:
        atributo = retornar_atributo_de_veiculos(opcao_de_atributo)
        veiculos = ordenar_lista_por_atributo(veiculos, atributo)

        opcao_de_ordem_de_listagem = pedir_opcao_de_ordem_de_listagem()

        if opcao_de_ordem_de_listagem != 0:
            veiculos = retornar_lista_em_ordem_desejada(veiculos, opcao_de_ordem_de_listagem)

            estrutura_inicial_de_menu()
            escrever_lista_de_veiculos(veiculos)
    else:
        opcao_de_ordem_de_listagem = 0

    return veiculos, opcao_de_ordem_de_listagem


# Operação de retornar o atributo de veículos que será tomado como referência para a ordenação, de acordo com a sua 
# nomenclatura no dicionário da lista.
def retornar_atributo_de_veiculos(opcao_de_atributo):
    if opcao_de_atributo == 1:
        return 'ulid'
    elif opcao_de_atributo == 2:
        return 'modelo_id'
    elif opcao_de_atributo == 3:
        return 'cor'
    elif opcao_de_atributo == 4:
        return 'ano_fabricacao'
    elif opcao_de_atributo == 5:
        return 'ano_modelo'
    elif opcao_de_atributo == 6:
        return 'valor'
    elif opcao_de_atributo == 7:
        return 'placa'
    
    return 'vendido'


# Operação de atualizar as informações de um veículo
def atualizar_veiculo(veiculos, ulid_do_veiculo_atualizado):
    for veiculo in veiculos:
        if veiculo['ulid'] == ulid_do_veiculo_atualizado:
            veiculo['cor'] = pedir_string('\n-> Digite a cor ATUALIZADA do veículo: ').upper()
            veiculo['ano_fabricacao'] = pedir_int_min_max('-> Digite o ano de fabricação do veículo: ', 1886, 2024)
            veiculo['ano_modelo'] = pedir_int_min_max('-> Digite o ano de fabricação do modelo do veículo: ', 1886, veiculo['ano_fabricacao'])
            veiculo['valor'] = pedir_float_min('-> Digite o valor ATUALIZADO do veículo: R$ ', 1000)
            veiculo['placa'] = pedir_string('-> Digite a placa ATUALIZADA do veículo: ').upper()
            break

    return veiculos


# Operação de filtrar os veículos de acordo com uma sequência de letras no nome de sua montadora.
def filtrar_veiculo_por_sequencia_da_montadora(veiculos, modelos_de_veiculos, montadoras, sequencia):
    veiculos_filtrados = []

    for montadora in montadoras:
        if sequencia in montadora['nome'].upper():
            for modelo in modelos_de_veiculos:
                if montadora['ulid'] == modelo['montadora_id']:
                    for veiculo in veiculos:
                        if veiculo['modelo_id'] == modelo['ulid']:
                            veiculos_filtrados.append(veiculo)

    return veiculos_filtrados


# Operação de filtrar os veículos de acordo com uma sequência de letras no nome de seu modelo.
def filtrar_veiculo_por_sequencia_do_modelo(veiculos, modelos_de_veiculos, sequencia):
    veiculos_filtrados = []

    for modelo in modelos_de_veiculos:
        if sequencia in modelo['nome'].upper():
            for veiculo in veiculos:
                if veiculo['modelo_id'] == modelo['ulid']:
                    veiculos_filtrados.append(veiculo)

    return veiculos_filtrados


# Operação de mostrar quantos veículos estão cadastrados
def mostrar_status_de_veiculos(veiculos):
    if len(veiculos) > 1:
        print(f'Temos {len(veiculos)} veículos cadastrados')
    else:
        print(f'Temos 1 veículo cadastrado')


# Operação de pedir que um usuário digite uma placa de veículo, verificando se a placa informada está registrada no sistema.
def pedir_placa_valida(texto, veiculos):
    placa_digitada = pedir_string(texto).upper()

    for veiculo in veiculos:
        if placa_digitada == veiculo['placa']:
            return placa_digitada
        
    return pedir_placa_valida(texto, veiculos)


# Operação de atribuir a opção de filtro escolhida pelo usuário à lista dos veículos
def retornar_filtro_de_veiculos(opcao_de_filtro):
    if opcao_de_filtro == 1:
        return 'cor'
    elif opcao_de_filtro == 2:
        return 'ano_fabricacao'
    elif opcao_de_filtro == 3:
        return 'ano_modelo'
    elif opcao_de_filtro == 4:
        return 'valor'
    elif opcao_de_filtro == 5 or opcao_de_filtro == 6:
        return 'vendido'
    
    return 'modelo_id'


# Operação de registrar um veículo como vendido de acordo com sua placa
def vender_veiculo(veiculos, placa_do_vendido):
    for veiculo in veiculos:
        if veiculo['placa'] == placa_do_vendido:
            veiculo['vendido'] = True
            break

    return veiculos


# Operação de criar duas sub-listas diferentes, uma para os veículos que foram vendidos e uma para os veículos que ainda não 
# foram vendidos.
def diferenciar_veiculos_por_venda(veiculos):
    if len(veiculos) > 0:
        veiculos_vendidos = filtrar(lambda veiculo: veiculo['vendido'], veiculos)
        veiculos_nao_vendidos = filtrar(lambda veiculo: not veiculo['vendido'], veiculos)
        return veiculos_vendidos, veiculos_nao_vendidos
    
    return [], []


# Verifica se existem veículos à venda de uma determinada montadora
def retornar_veiculos_disponiveis_por_montadora(veiculos_nao_vendidos, modelos_de_veiculos, montadoras, ulid_da_montadora_desejada):
    veiculos_disponiveis = []

    for montadora in montadoras:
        if montadora['ulid'] == ulid_da_montadora_desejada:
            for modelo in modelos_de_veiculos:
                if montadora['ulid'] == modelo['montadora_id']:
                    for veiculo in veiculos_nao_vendidos:
                        if veiculo['modelo_id'] == modelo['ulid']:
                            veiculos_disponiveis.append(veiculo)
            break # Evita repetições desnecessárias na lista após encontrar a montadora desejada

    return veiculos_disponiveis


# Operação de salvar os dados de veículos em arquivo .txt
def salvar_veiculos_em_txt(veiculos, nome_do_arquivo):
    if not path.exists('saves'):
        makedirs('saves')
    
    nome_do_arquivo = path.join('saves', nome_do_arquivo + '.txt')

    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in veiculos:
            linha = (
                f"ULID: {linha['ulid']} - ID do modelo: {linha['modelo_id']}\n"
                f"- Cor: {linha['cor']} - Ano de fabricação: {linha['ano_fabricacao']} - Ano do modelo: {linha['ano_modelo']}"
                f"- Valor: R$ {linha['valor']} - Placa: {linha['placa']} - Vendido: {linha['vendido']}\n\n"
            )
            arquivo.write(linha)


# Menu referente ao gerenciamento de veículos no sistema
def gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras):
    estrutura_de_gerenciador_de_veiculos('GERENCIADOR DE VEÍCULOS')
    opcao_de_gerenciador = pedir_int_min_max(INPUT_BASICO, 0, 7)
    nome_do_arquivo = 'veiculos'
    veiculos_vendidos, veiculos_nao_vendidos = diferenciar_veiculos_por_venda(veiculos)
    NUMERO_DE_ATRIBUTOS_DE_VEICULOS = 8
    CASAS_DECIMAIS = 2 # Casas decimais para valores float - EX: Valor do veículo
    QUANT_FILTROS_DE_VEICULOS = 8

    if opcao_de_gerenciador == 1: # Opção de registrar um novo veículo no sistema
        estrutura_inicial_de_menu()

        if len(modelos_de_veiculos) > 0:
            escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos)
            modelo_id = pedir_ulid_valido('\n-> Escolha um dos modelos listados pelo ULID (copie e cole para facilitar): ',
            modelos_de_veiculos)

            estrutura_inicial_de_menu()
            cor = pedir_string('-> Digite a cor do veículo: ').upper()
            ano_fabricacao = pedir_int_min_max('-> Digite o ano em que o veículo foi fabricado: ', 1886, 2024)
            ano_modelo = pedir_int_min_max('-> Digite o ano do modelo do veículo: ', 1886, ano_fabricacao)
            valor = pedir_float_min('-> Digite o preço do veículo: R$ ', 1000)
            placa = pedir_string('-> Digite a placa do veículo: ').upper()

            valor = truncar_casas_decimais(valor, CASAS_DECIMAIS)

            veiculos = criar_veiculo(veiculos, modelo_id, cor, ano_fabricacao, ano_modelo, valor, placa)
        else:
            erro(MENSAGEM_DE_NAO_CRIACAO_DE_NOVO_VEICULO)
        
        estrutura_final_de_menu()
        salvar_lista_em_json(veiculos, nome_do_arquivo)
        salvar_veiculos_em_txt(veiculos, nome_do_arquivo)
        return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)
    if opcao_de_gerenciador == 2: # Opção de listar os veículos já registrados
        if len(veiculos) > 0:
            veiculos, opcao_de_ordem_de_listagem = retornar_veiculos_ordenados(veiculos, 
            NUMERO_DE_ATRIBUTOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 3: # Opção de atualizar os dados de um veículo
        if len(veiculos) > 0:
            veiculos, opcao_de_ordem_de_listagem = retornar_veiculos_ordenados(veiculos, 
            NUMERO_DE_ATRIBUTOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                ulid_do_veiculo_atualizado = pedir_ulid_valido('\n-> Digite o ULID do veículo a ser atualizado (Copie e cole para facilitar): ',
                veiculos)
                veiculos = atualizar_veiculo(veiculos, ulid_do_veiculo_atualizado)
                estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 4: # Opção de remover um veículo do sistema
        if len(veiculos) > 0:
            veiculos, opcao_de_ordem_de_listagem = retornar_veiculos_ordenados(veiculos, NUMERO_DE_ATRIBUTOS_DE_VEICULOS)

            if opcao_de_ordem_de_listagem != 0:
                ulid_do_veiculo_removido = pedir_ulid_valido('-> Digite o ULID do veículo a ser removido (Copie e cole para facilitar): ',
                veiculos)
                confirmacao_de_remocao = retornar_valor_booleano('\n-> Você realmente quer remover esse veículo? S/N - ', 'S', 'N')

                if confirmacao_de_remocao:
                    veiculos = remover_item_de_lista(veiculos, ulid_do_veiculo_removido)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 5: # Opção de filtrar os veículos de acordo com atributos específicos
        if len(veiculos) > 0:
            opcao_de_filtro = pedir_opcao_de_filtro_de_lista(SUB_MENU_DE_FILTRO_DE_VEICULOS, QUANT_FILTROS_DE_VEICULOS)

            if opcao_de_filtro != 0:
                filtro = retornar_filtro_de_veiculos(opcao_de_filtro)

                if filtro == 'cor':
                    # Filtragem pela sequência de letras na cor do veículo
                    sequencia = pedir_string('\n-> Digite a sequência de letras a ser filtrada: ').upper()
                    veiculos_filtrados = filtrar(lambda veiculo: sequencia in veiculo['cor'].upper(), veiculos)
                elif filtro == 'ano_fabricacao':
                    # Filtragem por ano de fabricação do veículo
                    ano_fabricacao_a_filtrar = pedir_int_min_max('\n-> Digite o ano de fabricação de veículo a ser filtrado: ', 
                    1886, 2024)

                    limpar_tela()
                    print(SUB_MENU_DE_ANO_A_FILTRAR)
                    opcao_de_ano_fabricacao = pedir_int_min_max(INPUT_BASICO, 0, 3)

                    if opcao_de_ano_fabricacao == 1:
                        # Filtrar por ano exato
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_fabricacao'] == ano_fabricacao_a_filtrar, 
                        veiculos)
                    elif opcao_de_ano_fabricacao == 2:
                        # Filtrar por valores acima do ano escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_fabricacao'] > ano_fabricacao_a_filtrar,
                        veiculos)
                    elif opcao_de_ano_fabricacao == 3:
                        # Filtrar por valores abaixo do ano escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_fabricacao'] < ano_fabricacao_a_filtrar,
                        veiculos)
                    else:
                        return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)
                elif filtro == 'ano_modelo':
                    # Filtragem por ano de fabricação do modelo de veículo
                    ano_modelo_a_filtrar = pedir_int_min_max('\n-> Digite o ano de fabricação de veículo a ser filtrado: ', 
                    1886, 2024)

                    limpar_tela()
                    print(SUB_MENU_DE_ANO_A_FILTRAR)
                    opcao_de_ano_modelo = pedir_int_min_max(INPUT_BASICO, 0, 3)

                    if opcao_de_ano_modelo == 1:
                        # Filtrar por ano exato
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_modelo'] == ano_modelo_a_filtrar, 
                        veiculos)
                    elif opcao_de_ano_modelo == 2:
                        # Filtrar por valores acima do ano escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_modelo'] > ano_modelo_a_filtrar,
                        veiculos)
                    elif opcao_de_ano_modelo == 3:
                        # Filtrar por valores abaixo do ano escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['ano_modelo'] < ano_modelo_a_filtrar,
                        veiculos)
                    else:
                        return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)
                elif filtro == 'valor':
                    # Filtragem por valor de veículos
                    valor_a_filtrar = pedir_float_min('\n-> Digite um valor de veículo para ser filtrado: R$ ', 1000)

                    limpar_tela()
                    print(SUB_MENU_DE_VALOR_A_FILTRAR)
                    opcao_de_valor = pedir_int_min_max(INPUT_BASICO, 0, 3)

                    if opcao_de_valor == 1:
                        # Filtrar por valor exato
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['valor'] == valor_a_filtrar, 
                        veiculos)
                    elif opcao_de_valor == 2:
                        # Filtrar por valores acima do valor escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['valor'] > valor_a_filtrar,
                        veiculos)
                    elif opcao_de_valor == 3:
                        # Filtrar por valores abaixo do valor escolhido
                        veiculos_filtrados = filtrar(lambda veiculo: veiculo['valor'] < valor_a_filtrar,
                        veiculos)
                    else:
                        return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)
                elif filtro == 'vendido':
                    # Filtragem por venda de veículos
                    if opcao_de_filtro == 5:
                        veiculos_filtrados = veiculos_vendidos
                    else:
                        veiculos_filtrados = veiculos_nao_vendidos
                else:
                    # Filtragens que exigem o uso do id do modelo de veículo
                    sequencia = pedir_string('\n-> Digite a sequência de letras a ser filtrada: ').upper()

                    if opcao_de_filtro == 7:
                        # Filtragem por parte do nome da montadora 
                        veiculos_filtrados = filtrar_veiculo_por_sequencia_da_montadora(veiculos, modelos_de_veiculos, montadoras, 
                        sequencia)
                    else:
                        # Filtragem por parte do nome do modelo do veículo
                        veiculos_filtrados = filtrar_veiculo_por_sequencia_do_modelo(veiculos, modelos_de_veiculos, sequencia)

                if len(veiculos_filtrados) > 0:
                    veiculos_filtrados, opcao_de_ordem_de_listagem = retornar_veiculos_ordenados(veiculos_filtrados, 
                    NUMERO_DE_ATRIBUTOS_DE_VEICULOS)

                    if opcao_de_ordem_de_listagem != 0:
                        estrutura_final_de_menu()
                else:
                    estrutura_inicial_de_menu()
                    erro(MENSAGEM_DE_FILTRAGEM_VAZIA_DE_VEICULOS)
                    estrutura_final_de_menu()
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_VEICULOS_VAZIOS)
            estrutura_final_de_menu()
    elif opcao_de_gerenciador == 6: # Opção de mostrar o número de veículos registradas
        mensagem = (lambda: mostrar_status_de_veiculos(veiculos) if len(veiculos) > 0 else erro(MENSAGEM_DE_VEICULOS_VAZIOS))

        estrutura_inicial_de_menu()
        mensagem()
        estrutura_final_de_menu()
    elif opcao_de_gerenciador == 7: # Opção de marcar um veículo como vendido
        if len(veiculos_nao_vendidos) > 0:
            limpar_tela()
            print(SUB_MENU_DE_BUSCA_PARA_VENDA)
            opcao_de_busca_para_venda = pedir_int_min_max(INPUT_BASICO, 0, 3)

            if opcao_de_busca_para_venda != 0:
                if opcao_de_busca_para_venda == 1:
                    # Caso em que se busca veículos à venda de uma montadora em específico
                    estrutura_inicial_de_menu()
                    escrever_lista_de_montadoras(montadoras)

                    ulid_da_montadora_desejada = pedir_ulid_valido('\n-> Digite o ULID da montadora desejada (Copie e cole para facilitar): ', 
                    montadoras)

                    veiculos_disponiveis = retornar_veiculos_disponiveis_por_montadora(veiculos_nao_vendidos, modelos_de_veiculos, 
                    montadoras, ulid_da_montadora_desejada)   
                elif opcao_de_busca_para_venda == 2:
                    # Caso em que se busca veículos à venda de um modelo de veículo em específico
                    estrutura_inicial_de_menu()
                    escrever_lista_de_modelos_de_veiculos(modelos_de_veiculos)

                    ulid_do_modelo_desejado = pedir_ulid_valido('\n-> Digite o ULID do modelo de veículo desejado (Copie e cole para facilitar): ', 
                    modelos_de_veiculos)

                    veiculos_disponiveis = filtrar(lambda veiculo: veiculo['modelo_id'] == ulid_do_modelo_desejado, veiculos_nao_vendidos)
                else:
                    # Caso em que se busca todos os veículos que estão à venda
                    veiculos_disponiveis = veiculos_nao_vendidos
                
                if len(veiculos_disponiveis) > 0:
                        veiculos_disponiveis, opcao_de_ordem_de_listagem = retornar_veiculos_ordenados(veiculos_disponiveis, 
                        NUMERO_DE_ATRIBUTOS_DE_VEICULOS)

                        if opcao_de_ordem_de_listagem != 0:
                            print('\nO.B.S: Todos os veículos listados aqui estão à venda')
                            placa_do_vendido = pedir_placa_valida('-> Digite a placa do veículo desejado (copie e cole para facilitar): ',
                            veiculos_disponiveis)
                            veiculos = vender_veiculo(veiculos, placa_do_vendido)
                            estrutura_final_de_menu()
                else:
                    erro(MENSAGEM_DE_INDISPONIBILIDADE_DE_VEICULOS_ESPECIFICOS)
            else:
                return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)
        else:
            estrutura_inicial_de_menu()
            erro(MENSAGEM_DE_INDISPONIBILIDADE_DE_VEICULOS)
            estrutura_final_de_menu()
    else:
        limpar_tela()
        salvar_lista_em_json(veiculos, nome_do_arquivo)
        salvar_veiculos_em_txt(veiculos, nome_do_arquivo)

        return veiculos
    
    salvar_lista_em_json(veiculos, nome_do_arquivo)
    salvar_veiculos_em_txt(veiculos, nome_do_arquivo)
    return gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)

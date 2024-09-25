# Arquivo que reúne as funções e textos que são utilizadas por mais de um arquivo


from utils.io_utils import limpar_tela, enter_para_limpar_tela, pedir_int_min_max, pedir_string
from os import path, makedirs
from json import load, dump
from utils.vetor_utils import inverter_vetor, filtrar
from ulid import ULID

# Sub-menu referente à ordem de listagem (ascendente ou descendente)
SUB_MENU_DE_ORDEM_DE_LISTAGEM = '''
=======================================================================================================================================
| Digite 1 para ordenar de forma ASCENDENTE
| Digite 2 para ordenar de forma DESCENDENTE
| Digite 0 para voltar ao menu do gerenciador
=======================================================================================================================================
'''

# Mensagem básica de input usada diversas vezes
INPUT_BASICO = '-> Escolha uma das opções acima: '


# Estrutura básica compartilhada pelos gerenciadores do sistema (montadoras e modelos de veículos)
def estrutura_basica_de_gerenciador(titulo):
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
| 0. Voltar ao menu principal
=======================================================================================================================================
''')
    

# Estrutura que alguns dos menus do sistema contêm em seu início
def estrutura_inicial_de_menu():
    limpar_tela()
    print('=======================================================================================================================================')


# Estrutura que alguns dos menus do sistema contêm em seu fim
def estrutura_final_de_menu():
    print('=======================================================================================================================================')
    enter_para_limpar_tela()


# Operação de carregar os dados de algum arquivo para uma lista. Retorna uma lista vazia, caso não encontre nenhum
# arquivo válido.
def carregar_arquivo(nome_do_arquivo):
    nome_do_arquivo = path.join('saves', nome_do_arquivo + '.json')

    if path.exists(nome_do_arquivo):
        with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
            lista = load(arquivo, object_hook=converter_string_para_ulid)
    else:
        lista = []

    return lista
    

# Agregada de gerenciador_de_montadoras - Operação de retornar a lista de montadoras de acordo com a sua ordem de ascendência
# (Ascendente ou descendente).
def retornar_lista_em_ordem_desejada(lista, opcao_de_ordem_de_listagem):
    if opcao_de_ordem_de_listagem == 2: # 2 é a opção correspondente à ordem descendente
        lista = inverter_vetor(lista)

    return lista


# Agregada de gerenciador_de_montadoras - Operação de pedir que o usuário escolha uma das opções de filtragem apresentadas
def pedir_opcao_de_filtro_de_lista(sub_menu_de_filtro, quant_filtros):
    limpar_tela()
    print(sub_menu_de_filtro)
    opcao_de_filtro = pedir_int_min_max(INPUT_BASICO, 0, quant_filtros)

    return opcao_de_filtro


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


# Pede que o usuário digite um ulid, considerando-o válido caso ele exista em uma lista analisada
def pedir_ulid_valido(texto, lista):
    ulid_digitado = pedir_string(texto)

    for elemento in lista:
        if elemento['ulid'] == ulid_digitado:
            return ulid_digitado
        
    return pedir_ulid_valido(texto, lista)


# Operação de remover um item de uma lista através do seu ULID
def remover_item_de_lista(lista, ulid_do_item_removido):
    return filtrar(lambda item: item['ulid'] != ulid_do_item_removido, lista)


# Processo de salvar os dados de uma lista em um arquivo .json
def salvar_lista_em_json(lista, nome_do_arquivo):
    if not path.exists('saves'):
        makedirs('saves')
    
    nome_do_arquivo = path.join('saves', nome_do_arquivo + '.json')

    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        dump(lista, arquivo, ensure_ascii=False, indent=4, default=converter_ulid_para_string)

    
# Processo de converter uma chave ULID para string, permitindo assim que um ID seja manipulado pelos métodos JSON
def converter_ulid_para_string(ulid):
    if type(ulid) == ULID:
        return str(ulid)
    

# Processo de converter uma string de ULID de volta para o objeto ULID
def converter_string_para_ulid(lista):
    if type(lista['ulid']) == str:
        try:
           lista['ulid'] = ULID(lista['ulid']) 
        except ValueError:
            pass
    
    return lista


# Pede um valor string, retornando um valor True ou False equivalente, dependendo da resposta do usuário
def retornar_valor_booleano(texto, resposta_true, resposta_false):
    valor_str = pedir_string(texto).upper()

    if valor_str == resposta_true:
        return True
    elif valor_str == resposta_false:
        return False
    
    return retornar_valor_booleano(texto, resposta_true, resposta_false)


# Processo de converter um valor booleano para um valor equivalente em string
def converter_string_para_boolean(valor_str, equivalente_true):
    if valor_str == equivalente_true:
        return True
    
    return False

#Arquivo que reúne as funções padrões referentes a operações com vetores


from random import uniform, shuffle
from utils.io_utils import pedir_float_min_max, pedir_float
from utils.math_utils import truncar_casas_decimais


#Função padrão para a operação de mapear os valores de um vetor
def mapear(funcao, iteravel):
    return [funcao(item) for item in iteravel]


#Função padrão para a operação de filtrar os valores de um vetor
def filtrar(funcao, iteravel):
    return [item for item in iteravel if funcao(item)]


#Função padrão para a operação de reduzir os valores de um vetor a um único valor
def reduzir(funcao, iteravel, valor_inicial):
    resultado = valor_inicial

    for item in iteravel:
        resultado = funcao(item, resultado)

    return resultado


#Atribui valores a um vetor de maneira aleatória, dentro de um intervalo determinado de números
def inicializar_vetor_aleatoriamente_in_range(quant_elementos, limite_inferior, limite_superior):
    return [uniform(limite_inferior, limite_superior) for _ in range(quant_elementos)]


#Pede que o usuário faça a atribuição manual dos valores de um vetor, dentro de um intervalo determinado de números
def inicializar_vetor_manualmente_in_range(vetor, quant_elementos, limite_inferior, limite_superior):
    for cont in range(quant_elementos):
        num_temporario = pedir_float_min_max(f'Digite o valor do {cont + 1}º elemento da lista: ', limite_inferior, limite_superior)
        vetor.append(num_temporario)
    return vetor


#Atribui valores a um vetor a partir dos valores de um arquivo
def inicializar_vetor_com_arquivo(nome_do_arquivo):
    fin = open(nome_do_arquivo)
    return [line for line in fin]


#Trunca os valores de um vetor para uma quantidade específica de casas decimais
def truncar_casas_decimais_de_vetor(vetor, casas_decimais):
    return mapear(lambda item: truncar_casas_decimais(item, casas_decimais), vetor)


def escrever_elementos_do_vetor(vetor):
    for elemento in vetor:
        print(elemento)


#Escreve os valores de um vetor com suas respectivas posições
def escrever_vetor_e_posicoes(vetor):
    for index in range(len(vetor)):
        print(f'{index + 1}º: {vetor[index]}')


#Reseta todos os elemento de um vetor para um único valor padronizado
resetar_valores = lambda vetor, valor_padrao: list(mapear(lambda _: valor_padrao, vetor))


#Calcula o somatório dos valores de um vetor
def calcular_somatorio(vetor, valor_inicial):
    return reduzir(lambda valor_atual, valor_inicial: valor_inicial + valor_atual, vetor, valor_inicial)


#Cria um novo vetor contendo apenas números positivos, tendo como base um outro vetor
def criar_vetor_de_positivos(vetor_original):
    return filtrar(lambda item: item >= 0, vetor_original)


#Cria um novo vetor contendo apenas números negativos, tendo como base um outro vetor
def criar_vetor_de_negativos(vetor_original):
    return filtrar(lambda item: item < 0, vetor_original)


#Adiciona novos valores a um vetor já existente, dentro de um intervalo determinado de números
def adicionar_novos_valores_in_range(vetor, quant_novos_valores, limite_inferior, limite_superior):
    for cont in range(quant_novos_valores):
        valor_temporario = pedir_float_min_max(f'Digite o {cont + 1}º valor: ', limite_inferior, limite_superior)
        vetor.append(valor_temporario)

    return vetor


#Remove um ou mais elementos de um vetor pelo seu valor exato
def remover_valor_exato(vetor, valor_removido):
    return filtrar(lambda valor_atual: valor_atual != valor_removido, vetor)


#Remove um elemento de um vetor pelo seu índice
def remover_valor_por_indice(vetor, index_removido):
    return vetor.remove(vetor[index_removido])


#Edita um valor de um vetor pelo seu índice
def editar_valor_por_indice(vetor, indice, mensagem_de_input):
    vetor[indice] = pedir_float(mensagem_de_input)
    return vetor


#Edita um valor de vetor pelo seu índice, dentro de um intervalo delimitado de números
def editar_valor_por_indice_in_range(vetor, index, mensagem_de_input, limite_inferior, limite_superior):
    vetor[index] = pedir_float_min_max(mensagem_de_input, limite_inferior, limite_superior)
    return vetor[index]


#Encontra o menor valor de um vetor, retornando o primeiro valor caso todos sejam iguais
def retornar_menor_valor_de_vetor(vetor):
    valor_inicial = vetor[0]
    return reduzir(lambda menor_valor, valor_atual: valor_atual if valor_atual < menor_valor else menor_valor, vetor, valor_inicial)

 
#Encontra o maior valor de um vetor, retornando o primeiro valor caso todos sejam iguais
def retornar_maior_valor_de_vetor(vetor):
    valor_inicial = vetor[0]
    return reduzir(lambda maior_valor, valor_atual: valor_atual if valor_atual > maior_valor else maior_valor, vetor, valor_inicial)


#Retorna o primeiro index encontrado de um valor específico do vetor
def retornar_index(vetor, valor_especifico):
    for index in range(len(vetor)):
        if vetor[index] == valor_especifico:
            return index
        

#Multiplica todos os valores de um vetor por um valor específico
def multiplicar_valores_de_vetor(vetor, multiplicador):
    return mapear(lambda item: item * multiplicador, vetor)


#Eleva todos os valores de um vetor a um expoente específico (Exponenciação)
def elevar_valores_de_vetor(vetor, expoente):
    for cont in range(len(vetor)):
        if vetor[cont] == 0 and expoente < 0:
            continue
        else:
            vetor[cont] **= expoente

    return vetor


#Retorna a ordem inversa dos valores de um vetor
def inverter_vetor(vetor_original):
    return vetor_original[::-1]


#Embaralha a ordem dos valores de um vetor aleatoriamente
def embaralhar_vetor(vetor):
    shuffle(vetor)
    return vetor


#Salva os valores de um vetor em um arquivo, cada valor em uma linha diferente (Caso já exista um arquivo com
#o mesmo nome, o arquivo antigo será sobrescrito)
def salvar_vetor(vetor, nome_do_arquivo):
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        for valor in vetor:
            arquivo.write(f'{valor}\n')


#Salva os valores de um vetor em um arquivo, cada valor em uma linha diferente, garantindo que o formato do arquivo
#será EXCLUSIVAMENTE .txt (Caso já exista um arquivo com o mesmo nome, o arquivo antigo será sobrescrito)
def salvar_vetor_em_txt(vetor, nome_do_arquivo):
    with open(nome_do_arquivo + '.txt', 'w', encoding='utf-8') as arquivo:
        for valor in vetor:
            arquivo.write(f'{valor}\n')


#Converte os valores strings de um vetor para float
def converter_vetor_string_para_float(vetor):
    return mapear(lambda item: float(item), vetor)

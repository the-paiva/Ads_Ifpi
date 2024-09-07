from os import system

#Pede um valor string
def pedir_string(texto):
    return str(input(texto))

#Procedimento padrão para ler uma palavra em uma linha
def preparar_palavra(fin):
    return fin.readline().strip()

#Procedimento padrão para limpar a tela
def limpar_tela():
    system('cls')

#Procedimento padrão no qual o usuário pressiona ENTER para limpar a tela e seguir o fluxo da aplicação
def enter_para_limpar_tela():
    input('\n-> Pressione ENTER para continuar...')
    system('cls')

#Verifica se uma palavra tem mais de 20 letras
def tem_mais_letras(palavra, piso_de_letras):
    if len(palavra) > piso_de_letras:
        return True
    
    return False

#Verifica se uma letra de uma palavra é igual a uma letra de uma lista específica
def eh_letra_especifica(letra, lista_de_letras):
    for index in range(len(lista_de_letras)):
        if letra == lista_de_letras[index]:
            return True
        
    return False

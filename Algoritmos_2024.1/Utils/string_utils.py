#Arquivo que reúne as funções padrões referentes a operações com strings


from os import system


#Pede um valor string
pedir_string = lambda texto: str(input(texto))


#Procedimento padrão para ler uma palavra em uma linha
preparar_palavra = lambda fin: fin.readline().strip()


#Procedimento padrão para limpar a tela
limpar_tela = lambda: system('cls')


#Procedimento padrão no qual o usuário pressiona ENTER para limpar a tela e seguir o fluxo da aplicação
def enter_para_limpar_tela():
    input('\n-> Pressione ENTER para continuar...')
    system('cls')


#Verifica se uma palavra tem mais letras do que uma determinada quantidade de letras
tem_mais_letras = lambda palavra, piso_de_letras: True if len(palavra) > piso_de_letras else False


#Verifica se uma letra de uma palavra é igual a uma letra de uma lista específica
def eh_letra_especifica(letra, lista_de_letras):
    for index in range(len(lista_de_letras)):
        if letra == lista_de_letras[index]:
            return True
        
    return False

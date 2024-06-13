#Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo 
#deve escrever uma mensagem de permissão de acesso ou não.

from Utils.io_utils import pedir_int
from Utils.math_utils import eh_igual

def main():
    SENHA_CORRETA = 1234
    senha_fornecida = pedir_int('\nDigite a senha: ')

    if eh_igual(senha_fornecida, SENHA_CORRETA):
        print('\nAcesso permitido! Bem vindo!')
    else:
        print('\nAcesso negado!')
        main()

main()

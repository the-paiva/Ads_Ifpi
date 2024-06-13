#Leia uma letra, verifique se a letra é "F" ou "M" e escreva F - Feminino, M - Masculino, 
#Sexo Inválido.

from Utils.io_utils import pedir_string

def main():
    sexo = pedir_string('\nDigite o seu sexo (M/F): ')

    if sexo == 'M' or sexo == 'm':
        print('\nM - Masculino')
    elif sexo == 'F' or sexo == 'f':
        print('\nF - Feminino')
    else:
        print('\nSexo Inválido')

main()

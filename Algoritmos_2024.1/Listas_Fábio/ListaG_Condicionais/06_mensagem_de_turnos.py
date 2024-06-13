#Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
#escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

from Utils.io_utils import pedir_string

#Escreve uma mensagem de acordo com o turno digitado pelo usuário
def escrever_mensagem(turno):
    if turno == 'M' or turno == 'm':
        print('\nBom dia!')
    elif turno == 'V' or turno == 'v':
        print('\nBoa tarde!')
    elif turno == 'N' or turno == 'n':
        print('\nBoa noite!')
    else:
        print('\nValor Inválido!')

def main():
    turno = pedir_string('\nDigite o turno das suas aulas (M/V/N): ')
    escrever_mensagem(turno)

main()

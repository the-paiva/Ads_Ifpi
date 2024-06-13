#Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
#calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento - Conceito
#Entre 9.0 e 10.0             A
#Entre 7.5 e 9.0              B
#Entre 6.0 e 7.5              C
#Entre 4.0 e 6.0              D
#Entre 0 e 4.0                E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
#“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

from Utils.io_utils import pedir_float_min_max

#Atribui um conceito de nota ao aluno com base em sua média
def atribuir_conceito(media):
    if media >= 9:
        return 'A'
    elif media >= 7.5:
        return 'B'
    elif media >= 6.0:
        return 'C'
    elif media >= 4.0:
        return 'D'
    
    return 'E'

#Retorna a situação do aluno no semestre de acordo com o conceito alcançado
def retornar_situacao_do_aluno(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'APROVADO'
    
    return 'REPROVADO'

#Escreve um relatório descrevendo o desempenho do aluno
def escrever_relatorio_do_aluno(nota1, nota2, media, conceito, situacao_do_aluno):
    print('========================================')
    print(f'1ª nota  : {nota1:.2f}')
    print(f'2ª nota  : {nota2:.2f}')
    print(f'Média    : {media:.2f}')
    print(f'Conceito : {conceito}')
    print(f'Situação : {situacao_do_aluno}')

def main():
    NOTA_MINIMA = 0
    NOTA_MAXIMA = 10

    nota1 = pedir_float_min_max('\nDigite a 1ª nota do aluno: ', NOTA_MINIMA, NOTA_MAXIMA)
    nota2 = pedir_float_min_max('Digite a 2ª nota do aluno: ', NOTA_MINIMA, NOTA_MAXIMA)

    media = (nota1 + nota2) / 2
    conceito = atribuir_conceito(media)
    situacao_do_aluno = retornar_situacao_do_aluno(conceito)

    escrever_relatorio_do_aluno(nota1, nota2, media, conceito, situacao_do_aluno)

main()

#Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
#matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:
#
#   Média Final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10
#
#Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
#aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
#de alunos da turma.

from Utils.io_utils import pedir_int_min, pedir_float_min_max

#Atualiza a contagem de aprovados e reprovados na turma
def atualizar_contagens(media_final, cont_aprovados, cont_reprovados):
    if media_final >= 7:
        return cont_aprovados + 1, cont_reprovados
    else:
        return cont_aprovados, cont_reprovados + 1

#Mostra o relatório de aprovações e reprovações da turma
def mostrar_portaria(cont_alunos, cont_aprovados, cont_reprovados):
    print('\n============== PORTARIA ==============')
    print(f'Total geral de alunos: {cont_alunos}')
    print(f'Total de aprovados: {cont_aprovados}')
    print(f'Total de reprovados: {cont_reprovados}')
    print('======================================')

def main():
    matricula = -1
    cont_alunos, cont_aprovados, cont_reprovados = 0, 0, 0

    while matricula != 0:
        matricula = pedir_int_min('\nDigite a matrícula do aluno: ', 0)

        if matricula != 0:
            nota1 = pedir_float_min_max('Digite a 1ª nota do aluno: ', 0, 10)
            nota2 = pedir_float_min_max('Digite a 2ª nota do aluno: ', 0, 10)
            nota3 = pedir_float_min_max('Digite a 3ª nota do aluno: ', 0, 10)

            media_final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10
            cont_aprovados, cont_reprovados = atualizar_contagens(media_final, cont_aprovados, cont_reprovados)
            cont_alunos += 1

    mostrar_portaria(cont_alunos, cont_aprovados, cont_reprovados)

main()

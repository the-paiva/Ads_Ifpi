#Atividade V - Play Number


from io_utils import pedir_int_min_max
import vetor_funcionalidade


def main():
    digito = -1
    DIGITO_DE_SAIDA = 16
    vetor = []
    limite_inferior, limite_superior = 0, 0
    CASAS_DECIMAIS = 2

    while digito != DIGITO_DE_SAIDA:
        vetor_funcionalidade.menu_principal()
        digito = pedir_int_min_max('-> Escolha uma das opções listadas acima: ', 1, 16)

        if digito == 1:
            vetor, limite_inferior, limite_superior = vetor_funcionalidade.menu_de_inicializacao_de_vetor(CASAS_DECIMAIS)
        elif digito == 2:
            vetor_funcionalidade.menu_de_relatorio_de_valores(vetor)
        elif digito == 3:
            vetor = vetor_funcionalidade.menu_de_reset_de_valores(vetor, CASAS_DECIMAIS)
        elif digito == 4:
            vetor_funcionalidade.menu_de_quantidade_de_elementos(vetor)
        elif digito == 5:
            vetor_funcionalidade.menu_de_menor_e_maior_valor(vetor)
        elif digito == 6:
            vetor_funcionalidade.menu_de_somatorio(vetor)
        elif digito == 7:
            vetor_funcionalidade.menu_de_media_aritmetica(vetor)
        elif digito == 8:
            vetor_funcionalidade.menu_de_numeros_positivos(vetor)
        elif digito == 9:
            vetor_funcionalidade.menu_de_numeros_negativos(vetor)
        elif digito == 10:
            vetor = vetor_funcionalidade.menu_de_atualizacao_regrada(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS)
        elif digito == 11:
            vetor = vetor_funcionalidade.menu_de_adicao_de_novos_valores(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS)
        elif digito == 12:
            vetor = vetor_funcionalidade.menu_de_remocao_por_valor(vetor)
        elif digito == 13:
            vetor_funcionalidade.menu_de_remocao_por_posicao(vetor)
        elif digito == 14:
            vetor_funcionalidade.menu_de_edicao_por_posicao(vetor, limite_inferior, limite_superior, CASAS_DECIMAIS)
        elif digito == 15:
            vetor_funcionalidade.menu_de_salvar_arquivo(vetor)
        else:
            vetor_funcionalidade.sair_do_programa(vetor)


main()

# Atividade Y - Patrocars
# Arquivo principal do programa


from patrocars_utils import carregar_arquivo, INPUT_BASICO
from utils.io_utils import pedir_int_min_max
from gerenciador_de_montadoras import gerenciador_de_montadoras
from gerenciador_de_modelos_de_veiculos import gerenciador_de_modelos_de_veiculos
from gerenciador_de_veiculos import gerenciador_de_veiculos


# Menu principal do sistema
MENU_PRINCIPAL = '''
============================================================== PATROCARS ==============================================================
| Digite 1 para entrar no menu de gerenciamento de montadoras
| Digite 2 para entrar no menu de gerenciamento de modelos de veículos
| Digite 3 para entrar no menu de gerenciamento de veículos
| Digite 0 para sair do sistema
| O.B.S: Novos dados serão salvos automaticamente à medida em que forem criados
=======================================================================================================================================
'''


def main():
    montadoras = carregar_arquivo('montadoras')
    modelos_de_veiculos = carregar_arquivo('modelos_de_veiculos')
    veiculos = carregar_arquivo('veiculos')
    opcao_principal = -1

    while opcao_principal != 0: # Fluxo principal do sistema
        print(MENU_PRINCIPAL)
        opcao_principal = pedir_int_min_max(INPUT_BASICO, 0, 3)

        if opcao_principal == 1: # Menu de gerenciamento de montadoras
            montadoras, modelos_de_veiculos, veiculos = gerenciador_de_montadoras(montadoras, modelos_de_veiculos, veiculos)
        elif opcao_principal == 2: # Menu de gerenciamento de modelos de veículos
            modelos_de_veiculos, veiculos = gerenciador_de_modelos_de_veiculos(modelos_de_veiculos, montadoras, veiculos)
        elif opcao_principal == 3: # Menu de gerenciamento de veículos
            veiculos = gerenciador_de_veiculos(veiculos, modelos_de_veiculos, montadoras)


main()

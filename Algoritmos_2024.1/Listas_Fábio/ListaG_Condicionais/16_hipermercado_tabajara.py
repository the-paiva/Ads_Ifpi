#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#       Até 5 Kg                Acima de 5 Kg
#File R$ 4,90 por Kg           R$ 5,80 por Kg
#Alcatra R$ 5,90 por Kg        R$ 6,80 por Kg
#Picanha R$ 6,90 por Kg        R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o
#cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
#e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
#compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

from Utils.io_utils import pedir_string, pedir_float_min

#Escreve o cabeçalho do programa, informando os tipos de carne disponíveis e seus respectivos códigos
def escrever_cabecalho():
    print('=========== HIPERMERCADO TABAJARA =========================')
    print('Tipos de carne                           Código')
    print('Filé                                       F')
    print('Alcatra                                    A')
    print('Picanha                                    P')
    print('===========================================================')

#Pede o tipo de carne que vai ser comprado
def pedir_tipo_de_carne():
    tipo_de_carne = pedir_string('Escolha um tipo de carne: ').upper()

    if tipo_de_carne == 'F' or tipo_de_carne == 'A' or tipo_de_carne == 'P':
        return tipo_de_carne

    return pedir_tipo_de_carne()

#Retorna o preço do quilo da carne de acordo com o tipo informado pelo usuário
def retornar_preco_da_carne(tipo_de_carne):
    if tipo_de_carne ==  'F':
        return 4.9
    elif tipo_de_carne == 'A':
        return 5.9

    return 6.9

#Ajusta o preço do quilo do produto de acordo com a quantidade que está sendo comprada
def ajustar_preco_da_carne(quantidade_de_carne, preco_da_carne_original):
    if quantidade_de_carne >= 5:
        return preco_da_carne_original + 0.9
    
    return preco_da_carne_original

#Retorna o tipo de carne comprado de acordo com o código digitado pelo usuário
def retornar_tipo_de_carne_completo(tipo_de_carne):
    if tipo_de_carne == 'F':
        return 'Filé'
    elif tipo_de_carne == 'A':
        return 'Alcatra'
    
    return 'Picanha'

#Pergunta se a compra será feita com o cartão Tabajara
def pedir_cartao_tabajara():
    cartao_tabajara = pedir_string('Deseja comprar com o cartão Tabajara? (S/N) ').upper()

    if cartao_tabajara == 'S' or cartao_tabajara == 'N':
        return cartao_tabajara
    
    return pedir_cartao_tabajara()

#Gera o cupom fiscal da compra do usuário (Não inclui o possível valor com desconto)
def gerar_cupom_fiscal(tipo_de_carne_completo, quantidade_de_carne, valor_total):
    print('===========================================================')
    print(f'Tipo de carne: {tipo_de_carne_completo}')
    print(f'Quantidade de carne: {quantidade_de_carne:.2f} Kg')
    print(f'Valor total: R$ {valor_total:.2f}')

#Verifica se as compras foram feitas com o cartão Tabajara
def eh_compra_com_cartao(cartao_tabajara):
    if cartao_tabajara == 'S':
        return True
    
    return False

#Adiciona as informações relacionadas ao desconto do cartão no cupom fiscal
def adicionar_informacoes_do_desconto(desconto, valor_final):
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Valor final a ser pago: R$ {valor_final:.2f}')

def main():
    escrever_cabecalho()
    tipo_de_carne = pedir_tipo_de_carne()
    quantidade_de_carne = pedir_float_min('Digite a quantidade de carne que você irá comprar (Kg): ', 1)

    preco_da_carne = retornar_preco_da_carne(tipo_de_carne)
    preco_da_carne = ajustar_preco_da_carne(quantidade_de_carne, preco_da_carne)
    valor_total = quantidade_de_carne * preco_da_carne
    tipo_de_carne_completo = retornar_tipo_de_carne_completo(tipo_de_carne)

    cartao_tabajara = pedir_cartao_tabajara()

    gerar_cupom_fiscal(tipo_de_carne_completo, quantidade_de_carne, valor_total)

    if eh_compra_com_cartao(cartao_tabajara):
        desconto = valor_total * 5 / 100
        valor_final = valor_total - desconto
        adicionar_informacoes_do_desconto(desconto, valor_final)

main()

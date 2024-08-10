#Escreva um algoritmo que calcula o retorno de um investimento financeiro. O usuário deve informar
#quanto será investido por mês e qual será a taxa de juros mensal. O algoritmo deve informar o saldo do
#investimento após um ano (soma das aplicações mensais + juros compostos), e perguntar ao usuário se
#deseja calcular o ano seguinte, sucessivamente. Por exemplo, caso o usuário deseje investir R$ 100,00
#por mês, e tenha uma taxa de juros de 1% ao mês, o algoritmo forneceria a seguinte saída:
#Saldo do investimento após 1 ano: 1268.25
#Deseja processar mais um ano (S/N)?

from Utils.io_utils import pedir_float_min, pedir_string

#Calcula o saldo total ao final dos anos
def calcular_saldo_total(saldo_total, montante, juros_mensal):
    meses = 12

    while meses > 0:
        saldo_total += montante
        saldo_total += saldo_total * (juros_mensal / 100)
        meses -= 1

    return saldo_total

#Atribui o valor de continuidade a uma string
def pedir_sim_ou_nao():
    mais_um_ano = pedir_string('Deseja processar mais um ano (S/N)? ').upper()

    if mais_um_ano == 'S':
        return True
    elif mais_um_ano == 'N':
        return False
    
    return pedir_sim_ou_nao()

def main():
    mais_um_ano = True
    saldo_total = 0

    while mais_um_ano:
        montante = pedir_float_min('Quanto você deseja investir por mês? ', 0)
        juros_mensal = pedir_float_min('Qual é a taxa de juros mensal (em %)? ', 0)

        saldo_total += calcular_saldo_total(saldo_total, montante, juros_mensal)
        print(f'\nSaldo do investimento após mais um ano: R$ {saldo_total:.2f}')

        mais_um_ano = pedir_sim_ou_nao()

main()

#Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
#maior quadrado menor que 38 é 36 (quadrado de 6).

from Utils.io_utils import pedir_int_min

#Retorn o maior quadrado que seja menor ou igual ao número digitado pelo usuário
def retornar_quadrado_escolhido(n):
    for cont in range(n + 1):
        quadrado_atual = cont**2

        if quadrado_atual <= n:
            quadrado_escolhido = quadrado_atual
        else:
            return quadrado_escolhido

def main():
    n = pedir_int_min('Digite um número inteiro maior que 0: ', 1)

    quadrado_escolhido = retornar_quadrado_escolhido(n) #Não achei nome melhor do que esse
    raiz_quadrada_escolhida = quadrado_escolhido**0.5

    print(f'\nMaior quadrado menor ou igual a {n}: {quadrado_escolhido} (Quadrado de {raiz_quadrada_escolhida:.0f})')

main()

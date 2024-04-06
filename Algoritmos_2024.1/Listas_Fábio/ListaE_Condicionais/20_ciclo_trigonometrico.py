#Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
#quarto) em que o ângulo se localiza.

#Pede uma variável int
def pedir_int(texto):
    return int(input(texto))

#Verifica em qual quadrante um ângulo se localiza
def localizar_quadrante(angulo):
    if angulo >= 0 and angulo <= 90:
        return 'primeiro quadrante'
    elif angulo > 90 and angulo <= 180:
        return 'segundo quadrante'
    elif angulo > 180 and angulo <= 270:
        return 'terceiro quadrante'
    elif angulo > 270 and angulo <= 360:
        return 'quarto quadrante'
    else:
        return 'INVÁLIDO'
    
#Saída de dados para o caso de ângulo válido
def mostrar_resultado_valido(angulo, quadrante):
    print(f'\nO ângulo de {angulo}° está localizado no {quadrante}.')

#Saída de dados para o caso de ângulo inválido
def mostrar_resultado_invalido():
    print('O valor digitado é INVÁLIDO!')

def main():
    angulo = pedir_int('\nDigite o valor de um ângulo: ')
    quadrante = localizar_quadrante(angulo)

    if quadrante != 'INVÁLIDO':
        mostrar_resultado_valido(angulo, quadrante)
    else:
        mostrar_resultado_invalido()

main()

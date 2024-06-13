#Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 
#variáveis inteiras: hora e minuto). 
#Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo máximo de 
#duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
#seguinte.

from Utils.io_utils import pedir_int_min_max

#Calcula a duração entre a hora de início e a hora de fim
def calcular_duracao_horas(hora_inicio, hora_fim):
    if hora_fim > hora_inicio:
        return hora_fim - hora_inicio
    else:
        DURACAO_DE_UM_DIA = 24
        return DURACAO_DE_UM_DIA - hora_inicio + hora_fim

#Calcula a duração entre o minuto de início e o minuto de fim
def calcular_duracao_minutos(minuto_inicio, minuto_fim):
    if minuto_fim >= minuto_inicio:
        return minuto_fim - minuto_inicio
    else:
        DURACAO_DE_UMA_HORA = 60
        return DURACAO_DE_UMA_HORA - minuto_inicio + minuto_fim
    
#Ajusta o valor da duração das horas em casos específicos
def ajustar_duracao_horas(duracao_horas, minuto_fim, minuto_inicio):
    if minuto_fim < minuto_inicio:
        return duracao_horas - 1
    elif duracao_horas == 24:
        return 0

    return duracao_horas

#Verifica se a duração entre os horários é válida
def eh_duracao_valida(duracao_horas, duracao_minutos):
    if (duracao_horas == 0 and duracao_minutos == 0) or (duracao_minutos >= 30):
        return True
    
    return False

#Escreve a duração do jogo
def escrever_duracao(duracao_horas, duracao_minutos):
    if duracao_horas > 1 and duracao_minutos > 1:
        print(f'\nA duração do jogo foi de {duracao_horas} horas e {duracao_minutos} minutos.')
    elif duracao_horas > 1 and duracao_minutos == 1:
        print(f'\nA duração do jogo foi de {duracao_horas} horas e 1 minuto.')
    elif duracao_horas > 1 and duracao_minutos == 0:
        print(f'\nA duração do jogo foi de {duracao_horas} horas.')
    elif duracao_horas == 1 and duracao_minutos > 1:
        print(f'\nA duração do jogo foi de 1 hora e {duracao_minutos} minutos.')
    elif duracao_horas == 1 and duracao_minutos == 1:
        print(f'\nA duração do jogo foi de 1 hora e 1 minuto.')
    elif duracao_horas == 1 and duracao_minutos == 0:
        print(f'\nA duração do jogo foi de 1 hora.')
    elif duracao_horas == 0 and duracao_minutos == 0:
        print(f'\nA duração do jogo foi de 24 horas.')
    else:
        print(f'\nA duração do jogo foi de {duracao_minutos} minutos.')

#Reinicia o programa no caso em que a duração do jogo é inválida
def reiniciar_programa():
    print('\nDuração inválida! O jogo deve ter no mínimo 30 minutos de duração!')
    main()

def main():
    hora_inicio = pedir_int_min_max('\nDigite a hora de início do jogo: ', 0, 23)
    minuto_inicio = pedir_int_min_max('Digite o minuto de início do jogo: ', 0, 59)

    hora_fim = pedir_int_min_max('\nDigite a hora do fim do jogo: ', 0, 23)
    minuto_fim = pedir_int_min_max('Digite o minuto do fim do jogo: ', 0, 59)

    duracao_horas = calcular_duracao_horas(hora_inicio, hora_fim)
    duracao_minutos = calcular_duracao_minutos(minuto_inicio, minuto_fim)
    duracao_horas = ajustar_duracao_horas(duracao_horas, minuto_fim, minuto_inicio)

    if eh_duracao_valida(duracao_horas, duracao_minutos):
        escrever_duracao(duracao_horas, duracao_minutos)
    else:
        reiniciar_programa()

main()

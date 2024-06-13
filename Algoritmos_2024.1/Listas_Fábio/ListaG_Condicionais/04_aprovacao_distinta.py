#Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
#- "Aprovado", se a média alcançada for maior ou igual a sete;
#- "Reprovado", se a média for menor do que sete;
#- "Aprovado com Distinção", se a média for igual a dez.

from Utils.io_utils import pedir_float_min_max
from Utils.math_utils import calcular_media_aritmetica

#Verifica e retorna a situação do aluno de acordo com a sua média
def retornar_situacao_do_aluno(media):
    if media == 10:
        return 'Aprovado com Distinção'
    elif media >= 7:
        return 'Aprovado'
    
    return 'Reprovado'

#Escreve o relatório sobre a situação do aluno
def escrever_relatorio(media, situacao):
    print(f'\nMédia: {media:.2f}')
    print(f'Situação: {situacao}')

def main():
    nota1 = pedir_float_min_max('\nDigite a primeira nota do estudante: ', min=0, max=10)
    nota2 = pedir_float_min_max('Digite a segunda nota do estudante: ', min=0, max=10)
    
    somatorio = nota1 + nota2
    media = calcular_media_aritmetica(somatorio, quant_elementos=2)
    situacao = retornar_situacao_do_aluno(media)
    escrever_relatorio(media, situacao)

main()

#Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura**2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), 
#obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

#Pede um valor float com limite mínimo
def pedir_float_min_max(texto, min, max):
    num = float(input(texto))

    if num < min or num > max:
        num = pedir_float_min_max(texto, min, max)

    return num

#Calcula o IMC de acordo com o peso e a altura informados
def calcular_imc(peso, altura):
    return (peso / altura**2)

#Escreve a tabela de pesos do IMC
def escrevar_tabela_de_imc():
    print('')
    print('-' * 50)
    print('Tabela de IMC')
    print('-' * 50)
    print('Peso normal: Abaixo de 25')
    print('Obeso: Entre 25 e 30')
    print('Obesidade mórbida: Acima de 30')
    print('-' * 50)

#Escreve o resultado do IMC de acordo com os dados digitados pelo usuário
def escrever_resultado_do_imc(imc):
    print(f'\nSeu IMC: {imc:.2f}')

    if imc < 25:
        print('Parabéns! Você está no seu peso ideal!')
    elif imc <= 30:
        print('Cuidado! Você está obeso!')
    else:
        print('GRAVE! Você está em estado de obesidade mórbida!')

def main():
    altura = pedir_float_min_max('Digite a sua altura (em metros): ', 0.1, 3)
    peso = pedir_float_min_max('Digite o seu peso (em Kg): ', 0.1, 500)
    
    imc = calcular_imc(peso, altura)
    escrevar_tabela_de_imc()
    escrever_resultado_do_imc(imc)

main()

#Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores
#são diferentes.

#Pede uma variável do tipo int
def pedir_int(texto):
    return int(input(texto))

#Verifica qual é o maior entre dois números
def checar_maior_numero(a, b):
    if a > b:
        return a
    else:
        return b
    
#Verifica qual é o menor entre dois números
def checar_menor_numero(a, b):
    if a < b:
        return a
    else:
        return b
    
#Saída de dados do programa
def mostrar_resultado(maior, menor):
    if maior != menor:
        print(f'\n{maior} é o maior número digitado\n{menor} é o menor número digitado')
    else:
        print('\nTodos os números digitados são iguais')

def main():
    num1 = pedir_int('\nDigite o primeiro número: ')
    num2 = pedir_int('Digite o segundo número: ')
    num3 = pedir_int('Digite o terceiro número: ')
    num4 = pedir_int('Digite o quarto número: ')
    num5 = pedir_int('Digite o quinto número: ')

    maior = checar_maior_numero(num1, num2)
    maior = checar_maior_numero(maior, num3)
    maior = checar_maior_numero(maior, num4)
    maior = checar_maior_numero(maior, num5)

    menor = checar_menor_numero(num1, num2)
    menor = checar_menor_numero(menor, num3)
    menor = checar_menor_numero(menor, num4)
    menor = checar_menor_numero(menor, num5)

    mostrar_resultado(maior, menor)

main()

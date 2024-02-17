#Leia 3 números, calcule e escreva a média dos números.

#Entrada
num1 = float(input('\nDigite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

#Processamento
media = (num1 + num2 + num3) / 3

#Saída
print(f'\nMédia dos três números: {media:.2f}')

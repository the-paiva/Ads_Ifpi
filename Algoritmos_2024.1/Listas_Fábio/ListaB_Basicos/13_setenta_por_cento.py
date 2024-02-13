#Leia um valor em real (R$), calcule e escreva 70% deste valor.

#Entrada
valor = float(input('\nDigite um valor em real: R$ '))

#Processamento
porcentagem = valor * 70 / 100

#Saída
print(f'\n70% de R$ {valor:.2f}: R$ {porcentagem:.2f}')

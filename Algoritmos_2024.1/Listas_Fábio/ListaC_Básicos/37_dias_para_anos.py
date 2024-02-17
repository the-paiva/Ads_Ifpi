#Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

#Entrada
idade_dias = int(input('\nDigite a sua idade apenas em dias: '))

#Processamento
anos = idade_dias // 365
resto = idade_dias % 365

meses = resto // 30
dias = resto % 30

#Saída
print(f'\nIdade convertida: {anos} anos, {meses} meses e {dias} dias.')

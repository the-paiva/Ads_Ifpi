#Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a
#expressa apenas em dias.

#Entrada
anos = int(input('\nQuantos anos você tem? '))
meses = int(input('Quantos meses? '))
dias = int(input('Quantos dias? '))

#Processamento
anos_para_dias = anos * 365
meses_para_dias = meses * 30

dias_totais = anos_para_dias + meses_para_dias + dias

#Saída
print(f'\nVocê tem {dias_totais} dias de vida.')

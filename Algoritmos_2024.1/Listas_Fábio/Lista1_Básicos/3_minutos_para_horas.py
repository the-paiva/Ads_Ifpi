#Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#Entrada
valor_minutos = int(input('\nDigite uma quantidade de minutos: '))

#Processamento
valor_horas = valor_minutos // 60
minutos_restantes = valor_minutos % 60

#Saída
print(f'\n{valor_minutos} = {valor_horas} horas e {minutos_restantes} minutos')

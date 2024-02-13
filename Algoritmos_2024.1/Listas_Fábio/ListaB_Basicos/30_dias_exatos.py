#Leia um número inteiro de minutos, calcule e escreva quantos dias, 
#quantas horas e quantos minutos ele corresponde.

#Entrada
minutos = int(input('\nDigite um número inteiro de minutos: '))

#Processamento
dias = minutos // 1440
resto = minutos % 1440

horas = resto // 60
minutos_restantes = resto % 60

#Saída
print(f'\n{minutos} minutos equivalem a {dias} dias, {horas} horas e {minutos_restantes} minutos.')

#Leia um número inteiro de segundos, calcule e escreva quantas horas, 
#quantos minutos e quantos segundos ele corresponde.

#Entrada
segundos = int(input('\nDigite um número inteiro de segundos: '))

#Processamento
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

#Saída
print(f'\n{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.')

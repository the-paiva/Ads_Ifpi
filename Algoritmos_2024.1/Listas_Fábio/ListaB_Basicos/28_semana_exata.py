#Leia um número inteiro de horas, calcule e escreva quantas semanas,
#quantos dias e quantas horas ele corresponde.

#Entrada
horas = int(input('\nDigite uma quantidade inteira de horas: '))

#Processamento
semanas = horas // 168
resto = horas % 168
dias = resto // 24
horas_restantes = resto % 24

#Saída
print(f'\n{horas} horas equivalem a {semanas} semanas, {dias} dias e {horas_restantes} horas.')

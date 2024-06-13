#Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

#Entrada
valor_horas = int(input('\nDigite um valor em horas: '))
valor_minutos = int(input('Agora digite um valor em minutos: '))

#Processamento
horas_convertidas = valor_horas * 60
total_minutos = horas_convertidas + valor_minutos

#Saída
print(f'\n{valor_horas} horas * 60 = {horas_convertidas} minutos')
print(f'{horas_convertidas} + {valor_minutos} = {total_minutos} minutos')

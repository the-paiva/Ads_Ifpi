#Leia o valor da base e altura de um triângulo, calcule e escreva sua área.
#(área=(base * altura)/2)

#Entrada
base = float(input('\nDigite o valor da base do triângulo: cm '))
altura = float(input('Agora digite o valor da altura: cm '))

#Processamento
area = (base * altura) / 2

#Saída
print(f'\nÁrea: {area:.2f} cm')

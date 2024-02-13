#Leia o valor do raio de uma esfera, calcule e escreva seu volume.
#(v = (4 * pi * r**3) / 3) (pi = 3,14)

#Entrada
raio = float(input('\nDigite o valor do raio da esfera: cm '))

#Processamento
PI = 3.14
volume = (4 * PI * raio**3) / 3

#Saída
print(f'\nVolume total: {volume:.2f} cm')

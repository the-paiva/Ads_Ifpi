#Um sistema de equações lineares do tipo ax + by = c e dx + ey = f, pode ser resolvido 
#segundo mostrado abaixo:
#x = (c * e - b * f) / (a * e - b * d); y = (a * f - c * d) / (a * e - b * d)
#Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os 
#valores de x e y.

#Entrada
a = float(input('\nDigite o valor do coeficiente a: '))
b = float(input('Digite o valor do coeficiente b: '))
c = float(input('Digite o valor do coeficiente c: '))
d = float(input('Digite o valor do coeficiente d: '))
e = float(input('Digite o valor do coeficiente e: '))
f = float(input('Digite o valor do coeficiente f: '))

#Processamento
x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

#Saída
print(f'\nValor de x: {x:.2f}\nValor de y: {y:.2f}')
print(f'Equação linear: {a:.2f} * {x:.2f} + {b:.2f} * {y:.2f} = {c:.2f}')
print(' ' * 15, f'{d:.2f} * {x:.2f} + {e:.2f} * {y:.2f} = {f:.2f}')

#Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, 
#ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula
#abaixo:
#d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Entrada
x1 = int(input('\nDigite a coordenada de x1: '))
y1 = int(input('Digite a coordenada de y1: '))
x2 = int(input('Digite a coordenada de x2: '))
y2 = int(input('Digite a coordenada de y2: '))

#Processamento
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Saída
print(f'\nDistância entre o ponto 1 ({x1},{y1}) e o ponto 2 ({x2},{y2}): {d:.2f}')

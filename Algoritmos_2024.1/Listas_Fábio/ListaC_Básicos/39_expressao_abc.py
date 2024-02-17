#Leia três números inteiros e positivos (A, B, C) e calcule a seguinte 
#expressão: d = (r + s) / 2, onde r = (a + b)**2 e s = (b + c)**2.

#Entrada
print('\n--- Todos os números digitados devem ser inteiros e positivos ---\n')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#Processamento
r = (a + b)**2
s = (b + c)**2
d = (r + s) / 2

#Saída
print(f'\nr = ({a} + {b})**2\ns = ({b} + {c})**2')
print(f'd = ({r} + {s}) / 2 = {d:.2f}')

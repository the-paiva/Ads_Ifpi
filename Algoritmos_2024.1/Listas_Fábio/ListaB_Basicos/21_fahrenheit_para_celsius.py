#Leia uma temperatura em °F, calcule e escreva a equivalente em °C.
#(t°C = (5 * t°F - 160) / 9).

#Entrada
fahrenheit = int(input('\nDigite uma temperatura em graus Fahrenheit: °F '))

#Procssamento
celsius = int((5 * fahrenheit - 160) / 9)

#Saída
print(f'\n{fahrenheit} °F = {celsius} °C')

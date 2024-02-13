#Leia uma temperatura em °C, calcule e escreva a equivalente em °F.
#(t°F = (9 * t°C + 160) / 5)

#Entrada
celsius = int(input('\nDigite uma temperatura em graus Celsius: °C '))

#Processamento
fahrenheit = (9 * celsius + 160) / 5

#Saída
print(f'\n{celsius} °C = {fahrenheit} °F')

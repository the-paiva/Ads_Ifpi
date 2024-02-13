#Leia um valor em kg (quilograma), calcule e escreva o equivalente em
#g (grama).

#Entrada
kg = float(input('\nDigite um peso em quilogramas: kg '))

#Processamento
g = int(kg * 1000)

#Saída
print(f'\n{kg:.2f} kg = {g} g')

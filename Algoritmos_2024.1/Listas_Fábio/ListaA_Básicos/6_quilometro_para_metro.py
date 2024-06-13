#Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

#Entrada
velocidade_kmh = float(input('\nDigite uma velocidade em quilômetros por hora(Km/h): '))

#Processamento
velocidade_ms = velocidade_kmh / 3.6

#Saída
print(f'\n{velocidade_kmh:.2f} km/h = {velocidade_ms:.2f} m/s')

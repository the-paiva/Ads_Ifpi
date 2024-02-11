# Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

#Entrada
velocidade_ms = float(input('\nDigite uma velocidade em metros por segundo(m/s): '))

#Processamento
velocidade_kmh = velocidade_ms * 3.6

#Saída
print(f'\n{velocidade_ms:.2f} m/s = {velocidade_kmh:.2f} km/h')

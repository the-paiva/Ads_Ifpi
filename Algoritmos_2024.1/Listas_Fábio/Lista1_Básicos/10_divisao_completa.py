#Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão
# do 1º pelo 2º.

#Entrada
num_a = int(input('\nDigite o 1º número: '))
num_b = int(input('Digite o 2º número: '))

#Processamento
quociente = num_a // num_b
resto = num_a % num_b

#Saída
print(f'\nDivisão: {num_a} / {num_b}')
print(f'Quociente: {quociente}\nResto: {resto}')

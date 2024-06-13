#Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

#Entrada
num_a = int(input('\nDigite o 1º número: '))
num_b = int(input('Digite o 2º número: '))
num_c = int(input('Digite o 3º número: '))

#Processamento
soma = num_a + num_b
diff = num_b - num_c

#Saída
print('\nSoma de {} + {} = {}'.format(num_a, num_b, soma))
print('Diferença de {} - {} = {}'.format(num_b, num_c, diff))

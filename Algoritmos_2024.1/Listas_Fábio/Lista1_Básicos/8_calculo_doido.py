#Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

#Entrada
num_a = int(input('\nDigite o 1º número: '))
num_b = int(input('Digite o 2º número: '))

#Processamento
soma = num_a + num_b
diferenca = num_a - num_b
divisao = int(soma / diferenca)

#Saída
print(f'\n{num_a} + {num_b} = {soma}\n{num_a} - {num_b} = {diferenca}')
print(f'{soma} / {diferenca} = {divisao}')

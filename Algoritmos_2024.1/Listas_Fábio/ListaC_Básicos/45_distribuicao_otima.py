#Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
#decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que 
#realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas
#de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a 
#maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de 
#R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e
#duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e retorne a
#distribuição das notas de acordo com o critério da distribuição ótima.

#Entrada
print('\nNotas disponíveis: R$ 50, R$ 10, R$ 5, R$ 1\n')
valor = int(input('Digite a quantia que você deseja sacar: R$ '))

#Processamento
nota50 = valor // 50
resto50 = valor % 50

nota10 = resto50 // 10
resto10 = resto50 % 10

nota5 = resto10 // 5

nota1 = resto10 % 5

#Saída
print(f'\nNotas de R$ 50: {nota50}\nNotas de R$ 10: {nota10}')
print(f'Notas de R$ 5: {nota5}\nNotas de R$ 1: {nota1}')

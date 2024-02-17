#Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas 
#frações, escrevendo o resultado em forma de fração.

#Entrada
numerador1 = int(input('\nDigite o numerador da primeira fração: '))
denominador1 = int(input('Digite o denominador da primeira fração: '))
numerador2 = int(input('Digite o numerador da segunda fração: '))
denominador2 = int(input('Digite o denominador da segunda fração: '))

#Processamento
numerador = numerador1 + numerador2
denominador = denominador1 + denominador2

#Saída
print(f'\n{numerador1}/{denominador1} + {numerador2}/{denominador2}', end = ' ')
print(f' = {numerador}/{denominador}')

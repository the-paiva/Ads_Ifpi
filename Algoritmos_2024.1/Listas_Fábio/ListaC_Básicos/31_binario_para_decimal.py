#Leia um número inteiro (4 dígitos binários), calcule e escreva o 
#equivalente na base decimal.

#Entrada
binario = int(input('\nDigite um número inteiro binário: '))

#Processamento
digito1 = binario // 1000
resto1 = binario % 1000

digito2 = resto1 // 100
resto2 = resto1 % 100

digito3 = resto2 // 10
digito4 = resto2 % 10

decimal = digito1 * 2**3 + digito2 * 2**2 + digito3 * 2**1 + digito4 * 2**0

#Saída
print(f'\n{digito1}{digito2}{digito3}{digito4} na forma decimal: {decimal}')

#Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com 
#seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

#Entrada
num = int(input('\nDigite um número inteiro de 3 dígitos: '))

#Processamento
centena = str(num // 100)
resto = num % 100

dezena = str(resto // 10)
unidade = str(resto % 10)

num_inverso = int(unidade + dezena + centena)
soma = num + num_inverso

#Saída
print(f'\n{num} + {num_inverso} = {soma}')

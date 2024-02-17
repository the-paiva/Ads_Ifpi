#Leia um número inteiro (3 dígitos), calcule e escreva a diferença 
#entre o número e seu inverso.

#Entrada
num = int(input('\nDigite um número inteiro de três dígitos: '))

#Processamento
centena = str(num // 100)
resto = num % 100

dezena = str(resto // 10)
unidade = str(resto % 10)

num_inverso = int(unidade + dezena + centena)
diferenca = num - num_inverso

#Saída
print(f'\n{num} - {num_inverso} = {diferenca}')

#Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus 
#elementos (C + D + U).

#Entrada
num = int(input('\nDigite um número inteiro de até três dígitos: '))

#Processamento
centena = num // 100
resto = num % 100

dezena = resto // 10
unidade = resto % 10

soma = centena + dezena + unidade

#Saída
print(f'\nSoma de todos os dígitos: {centena} + {dezena} + {unidade} = {soma}')

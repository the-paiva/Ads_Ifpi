#Leia um número inteiro de meses, calcule e escreva quantos anos e 
#quantos meses ele corresponde.

#Entrada
meses = int(input('\nDigite um número inteiro de meses: '))

#Processamento
ano = meses // 12
meses_restantes = meses % 12

#Saída
print(f'\n{meses} meses equivalem a {ano} anos e {meses_restantes} meses.')

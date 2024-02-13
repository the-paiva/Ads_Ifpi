#Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ;
#inverso = 235)

#Entrada
num = int(input('\nDigite um número inteiro de três dígitos: '))

#Processamento
centena = num // 100
resto = num % 100

dezena = resto // 10
unidade = resto % 10

#Saída
print(f'\nNúmero inverso: {unidade}{dezena}{centena}')

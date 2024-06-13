#Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

#Entrada
cotacao = float(input('\nDigite a cotação atual do dólar: '))
valor_dolar = float(input('Agora digite um valor em dólar: USD '))

#Processamento
valor_real = valor_dolar * cotacao

#Saída
print(f'\nUSD {valor_dolar:.2f} = R$ {valor_real:.2f}')

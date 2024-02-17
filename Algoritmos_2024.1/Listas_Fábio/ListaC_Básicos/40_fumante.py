#Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número 
#de anos que ele fuma, o número de cigarros fumados por dia e o preço de uma 
#carteira (1 carteira tem 20 cigarros).

#Entrada
anos = int(input('\nHá quantos anos você fuma? '))
quant_cigarros = int(input('Quantos cigarros você fuma por dia? '))
preco_carteira = float(input('Digite o preço de uma carteira de cigarro: R$ '))

#Processamento
ANO_EM_DIA = 365 #Quantidade de dias em um ano
cigarros_totais = anos * ANO_EM_DIA * quant_cigarros
carteiras_totais = cigarros_totais // 20
dinheiro_gasto = carteiras_totais * preco_carteira

#Saída
print(f'\nCigarros fumados no total: {cigarros_totais}')
print(f'Carteiras compradas no total: {carteiras_totais}')
print(f'Dinheiro gasto no total: R$ {dinheiro_gasto:.2f}')

#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem
#do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a
#porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que
#leia o custo de fábrica de um carro e escreva o custo ao consumidor.

#Entrada
preco_fabrica = float(input('\nDigite o custo de fábrica do carro: R$ '))

#Processamento
taxa_distribuidor = preco_fabrica * 28 / 100
imposto = preco_fabrica * 45 / 100
preco_final = preco_fabrica + taxa_distribuidor + imposto

#Saída
print(f'\nPreço de fábrica: R$ {preco_fabrica:.2f}')
print(f'Taxa do distribuidor: R$ {taxa_distribuidor:.2f}')
print(f'Impostos: R$ {imposto:.2f}')
print(f'Preço final: R$ {preco_final:.2f}')

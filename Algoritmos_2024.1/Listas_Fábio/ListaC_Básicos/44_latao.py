#Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo 
#que calcule aquantidade de cada um desses componentes para se obter certa quantidade
#de latão (em kg), informada pelo usuário.

#Entrada
kg_latao = float(input('\nDigite uma quantidade de latão: Kg '))

#Processamento
cobre = kg_latao * 70 / 100
zinco = kg_latao * 30 / 100

#Saída
print(f'\nQuantidade de cobre: {cobre:.2f} kg')
print(f'Quantidade de zinco: {zinco:.2f} kg')

#Leia um número inteiro de metros, calcule e escreva quantos Km e
#quantos metros ele corresponde.

#Entrada
m = int(input('\nDigite um número inteiro de metros: m '))

#Processamento
km = m // 1000
m_restantes = m % 1000

#Saída
print(f'\n{m} m = {km} km e {m_restantes} m')

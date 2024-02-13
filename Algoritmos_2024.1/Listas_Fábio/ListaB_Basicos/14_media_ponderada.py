#Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

#Entrada
nome = input('\nDigite o nome do(a) estudante: ')
nota1 = float(input('Digite a primeira nota: '))
peso1 = int(input('Digite o peso da primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = int(input('Digite o peso da segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso3 = int(input('Digite o peso da terceira nota: '))

#Processamento
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

#Saída
print(f'\nEstudante: {nome}\nMédia ponderada: {media:.2f}')

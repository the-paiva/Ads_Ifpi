#Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

#Entrada
salario_velho = float(input('\nDigite o seu salário: '))

#Processamento
reajuste = salario_velho * 25 / 100
salario_novo = salario_velho + reajuste

#Saída
print(f'\nAumento: R$ {reajuste:.2f}\nNovo salário: R$ {salario_novo:.2f}')

#Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas 
#for maior ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame 
#e calcule a média final. Se esta média for maior ou igual a 5,0, o programa deve escrever
#“Aprovado”, caso contrário deve escrever “Reprovado”. Escreva um algoritmo para ler um número e 
#verificar se ele obedece a esta característica.

#Pede um valor float
def pedir_float(texto):
    return float(input(texto))

#Calcula a média das notas
def calcular_media(n1, n2):
    return (n1 + n2) / 2

#Verifica se a nota digitada é suficiente para que o aluno seja aprovado
def eh_media_aprovativa(media, media_aprovativa):
    if media >= media_aprovativa:
        return True
    
    return False

def main():
    nota1 = pedir_float('\nDigite a primeira nota do aluno: ')
    nota2 = pedir_float('Digite a segunda nota: ')
    media = calcular_media(nota1, nota2)

    print(f'\nMédia: {media:.2f}')

    if eh_media_aprovativa(media, 7):
        print('Situação: APROVADO')
    else:
        print('Situação: PROVA FINAL')
        nota_final = pedir_float('Digite a nota da prova final: ')
        media_final = calcular_media(media, nota_final)

        print(f'\nMédia final: {media_final:.2f}')

        if eh_media_aprovativa(media_final, 5):
            print('Situação: APROVADO')
        else:
            print('Situação: REPROVADO')

main()

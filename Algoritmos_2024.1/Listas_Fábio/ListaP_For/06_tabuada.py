#Escreva a tabuada dos números de 1 a 10.

def main():
    for num in range(1, 11):
        print(f'\nTabuada de {num} (soma)')

        for cont in range(1, 11):
            print(f'{num} x {cont} = {num * cont}')

main()

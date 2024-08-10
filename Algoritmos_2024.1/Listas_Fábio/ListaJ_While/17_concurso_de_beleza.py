#Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um
#algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais
#baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').

from Utils.io_utils import pedir_string, pedir_float_min_max

#Verifica se a candidata atual é a mais magra e retorna nome e peso
def verificar_candidata_mais_magra(nome, peso, candidata_mais_magra, menor_peso):
    if peso < menor_peso:
        return nome, peso
    
    return candidata_mais_magra, menor_peso

#Verifica se a candidata atual é a mais gorda e retorna nome e peso
def verificar_candidata_mais_gorda(nome, peso, candidata_mais_gorda, maior_peso):
    if peso > maior_peso:
        return nome, peso
    
    return candidata_mais_gorda, maior_peso

#Verifica se a candidata atual é a mais baixa e retorna nome e peso
def verificar_candidata_mais_baixa(nome, altura, candidata_mais_baixa, menor_altura):
    if altura < menor_altura:
        return nome, altura
    
    return candidata_mais_baixa, menor_altura

#Verifica se a candidata atual é a mais alta e retorna nome e peso
def verificar_candidata_mais_alta(nome, altura, candidata_mais_alta, maior_altura):
    if altura > maior_altura:
        return nome, altura
    
    return candidata_mais_alta, maior_altura

#Mostra os resultados relacionados às candidatas
def mostrar_resultados(candidata_mais_magra, menor_peso, candidata_mais_gorda, maior_peso, candidata_mais_baixa, menor_altura,
candidata_mais_alta, maior_altura):
    print('\n======================= RESULTADO =======================')
    print(f'Candidata mais magra: {candidata_mais_magra}')
    print(f'Peso da candidata mais magra: {menor_peso:.2f} Kg')
    print(f'\nCandidata mais gorda: {candidata_mais_gorda}')
    print(f'Peso da candidata mais gorda: {maior_peso:.2f} Kg')
    print(f'\nCandidata mais baixa: {candidata_mais_baixa}')
    print(f'Altura da candidata mais baixa: {menor_altura:.2f} m')
    print(f'\nCandidata mais alta: {candidata_mais_alta}')
    print(f'Altura da candidata mais alta: {maior_altura} m')

def main():
    nome = ''
    candidata_mais_magra, candidata_mais_gorda, candidata_mais_baixa, candidata_mais_alta = '', '', '', ''
    count = 0
    menor_peso, menor_altura = 999, 999
    maior_peso, maior_altura = 0, 0

    while nome != 'FIM':
        print(f'\nCartão da {count + 1}ª candidata')
        nome = pedir_string(f'Digite o nome da candidata: ').upper()

        if nome != 'FIM':
            altura = pedir_float_min_max('Digite a altura da candidata: ', 1, 3)
            peso = pedir_float_min_max('Digite o peso da candidata: ', 30, 200)

            candidata_mais_magra, menor_peso = verificar_candidata_mais_magra(nome, peso, candidata_mais_magra, menor_peso)
            candidata_mais_gorda, maior_peso = verificar_candidata_mais_gorda(nome, peso, candidata_mais_gorda, maior_peso)
            candidata_mais_baixa, menor_altura = verificar_candidata_mais_baixa(nome, altura, candidata_mais_baixa, menor_altura)
            candidata_mais_alta, maior_altura = verificar_candidata_mais_alta(nome, altura, candidata_mais_alta, maior_altura)

            count += 1

    if count >= 1:
        mostrar_resultados(candidata_mais_magra, menor_peso, candidata_mais_gorda, maior_peso, candidata_mais_baixa, menor_altura,
        candidata_mais_alta, maior_altura)
    else:
        print('\nNenhuma candidata foi registrada!')

main()

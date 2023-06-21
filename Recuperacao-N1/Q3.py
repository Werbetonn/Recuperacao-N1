print("\nSe você tiver 20 anos ou menos ganha um desconto de 15%, caso seja maior de 21 anos, ganha um desconto de 10%")

def calcular_desconto():

    idade = int(input('\nQual a sua idade: '))

    if idade <=20:
        print('\nVocê ganhou um desconto de 15%')
    else:
        print('\nVocê ganhou um desconto de 10%')

calcular_desconto()

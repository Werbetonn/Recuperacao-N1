import random

x = random.randrange(1,50)

print('\nInforme seu palpite no campo abaixo como número inteiro e tente a sorte')

palpite = None

while palpite != x:
    palpite = int(input('Qual o seu palpite?: '))
    if palpite == x:
        print('Parabéns, você acertou!')
    if palpite < x:
        print('Tente um palpite maior:')
    elif palpite > x:
        print('Tente um palpite menor:')

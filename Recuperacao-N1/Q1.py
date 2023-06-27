print('\nDigite seu cupom no campo abaixo e verifique se o mesmo é válido')

cupom = int(input("\nDigite o número do cupom: "))
CUPOM_INICIAL = 75
CUPOM_FINAL = 208
if CUPOM_INICIAL <= cupom <= CUPOM_FINAL:
    print('\nCupom válido')
else:
    print('\nCupom inválido')

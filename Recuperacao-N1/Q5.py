print('\nInsira as notas no campo abaixo para calcular a média da turma: ')

total = 0
for aluno in range(10):
    nota = float(input(f'\nInforme a nota do {aluno+1}° aluno :'))
    total = total + nota
    aluno +=1
media = total/aluno
print(f'A média da turma é {media}')

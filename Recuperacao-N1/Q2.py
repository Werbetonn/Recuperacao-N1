rank = {}
quantidade = int(input('Quantos livros deseja adicionar? '))
for i in range(quantidade):

    livro = input('Digite o nome de um livro: ')
    posicao = input('Digite a posição desse livro: ')

    rank[livro]=posicao

for livro, posicao in sorted(rank.items()):
    print(f'{posicao}- {livro}')

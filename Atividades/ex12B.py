# Faça 4 listas:
#     A. Filmes
#     B. Jogos
#     C. Livros
#     D. Esporte
#
# a. Adicione no mínimo 2 itens em cada lista.
# b. Crie uma lista das 4 listas criadas acima.
# c. Acesse (mostrar) algum item da lista livros.
# d. Remova um item da lista esporte.

filmes = []
filmes.append(input('Digite o nome de um filme: '))
filmes.append(input('Digite o nome de um filme: '))

jogos = []
jogos.append(input('Digite o nome de um jogo: '))
jogos.append(input('Digite o nome de um jogo: '))

livros = []
livros.append(input('Digite o nome de um livro: '))
livros.append(input('Digite o nome de um livro: '))

esporte = []
esporte.append(input('Digite o nome de um esporte: '))
esporte.append(input('Digite o nome de um esporte: '))

conjunto = [filmes, jogos, livros, esporte]

print(f"Livro 1: {livros[0]}")
esporte.pop(0)

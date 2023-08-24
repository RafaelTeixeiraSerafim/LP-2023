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
filmes.append(input())
filmes.append(input())

jogos = []
jogos.append(input())
jogos.append(input())

livros = []
livros.append(input())
livros.append(input())

esporte = []
esporte.append(input())
esporte.append(input())

conjunto = [filmes, jogos, livros, esporte]

print(f"Livro: {livros[0]}")
esporte.pop(0)

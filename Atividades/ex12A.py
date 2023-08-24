from collections import defaultdict

# Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
# os itens repetidos. 

lista = [1, 2, 1, 4, 5, 5, 9, 0, 1, 9]
count = defaultdict(int)

for i in lista:
    count[i] += 1

for key in count:
    if count[key] > 1:
        print(key)
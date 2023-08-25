# Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
# os itens repetidos. 

from collections import defaultdict

lista = []
n = int(input('Digite quantos itens você quer adicionar à lista: '))

for i in range(n):
    lista.append(input('Digite um item: '))

count = defaultdict(int)

for i in lista: 
    count[i] += 1

for key in count:
    if count[key] > 1:
        print(f'O item {key} repetiu {count[key]} vezes')
# Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles

lista = []

for i in range(5):
    lista.append(int(input('Digite um número inteiro: ')))

print(f'A soma dos números é {sum(lista)}')
# Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
# valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
# não continuar a escrever valores.

soma = 0
maior = 0
menor = float('inf')
cont = 0

while True:
    x = input('Digite um número inteiro ou (s) para sair: ')

    if x == 's':
        break
    
    x = int(x)

    maior = max(maior, x)
    menor = min(menor, x)
    soma += x
    cont += 1

if cont == 0:
    print('Nenhum número digitado')
else:
    media = soma / cont
    print(f'Média: {media}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
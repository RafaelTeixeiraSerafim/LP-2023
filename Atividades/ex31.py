# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
# perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.

import random

vitorias = 0
while True:
    paridade = input('\nEscolha impar ou par: ')
    num1 = int(input('Digite um número entre 1 e 100: '))

    num2 = random.randint(1, 100)
    print(f'Número do computador: {num2}')

    res = num1 + num2
    print(f'Soma: {res}')

    if res % 2 == 0 and paridade == 'par' or res % 2 == 1 and paridade == 'impar':
        print('Você ganhou!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break

print(f'Número de vitórias consecutivas: {vitorias}')
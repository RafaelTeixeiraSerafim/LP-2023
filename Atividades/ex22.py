# Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
# digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
# Desconsiderando o valor 1000 da parada.

soma = 0
cont = 0
while True:
    num = int(input('Digite um número inteiro: '))

    if num == 1000:
        break
    
    soma += num
    cont += 1

print(f'Soma: {soma}')
print(f'Número digitados: {cont}')

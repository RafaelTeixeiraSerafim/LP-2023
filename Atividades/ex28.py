# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
# cada eleitor votar e ao final mostrar o número de votos de cada candidato.

num = int(input('Digite o número de eleitores: '))

joao = carlos = maria = 0

for _ in range(num):
    voto = int(input('\nEscolha um para votar: \n1- João \n2- Carlos \n3- Maria\n'))

    if voto == 1:
        joao += 1
    elif voto == 2:
        carlos += 1
    elif voto == 3:
        maria += 1

print(f'\nJoão: {joao}')
print(f'Carlos: {carlos}')
print(f'Maria: {maria}')
# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
# códigos utilizados são:
# 1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# a. O total de votos para cada candidato;
# b. O total de votos nulos;
# c. O total de votos em branco;
# d. A percentagem de votos nulos sobre o total de votos;
# e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
# valor zero

carlos = mauricio = fernanda = ricardo = nulo = total = 0

while True:
    voto = int(input('\nEscolha um para votar: \n1- Carlos \n2- Maurício \n3- Fernanda \n4- Ricardo \n5- Nulo \n6- Sair \n'))

    if voto == 1:
        carlos += 1
    elif voto == 2:
        mauricio += 1
    elif voto == 3:
        fernanda += 1
    elif voto == 4:
        ricardo += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        break

    total += 1

print(f'\nNúmero de votos: {total}')
print(f'Carlos: {carlos}')
print(f'Maurício: {mauricio}')
print(f'Fernanda: {fernanda}')
print(f'Ricardo: {ricardo}')
print(f'Nulo: {nulo}')
print(f'Porcentagem de votos nulos: {nulo * 100 / total}')
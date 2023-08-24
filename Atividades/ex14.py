# Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.

lista = [1, 2, 3, 4, 5]

x = 3

if x in lista:
    print(lista.index(x))
else:
    print('Não está na lista')
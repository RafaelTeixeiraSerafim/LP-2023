# Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.

lista = []

for i in range(5):
    lista.append(input('Digite um item: '))

x = input('\nDigite um item para procurar: ')

if x in lista:
    print(f'Esse item está na posição {lista.index(x)} da lista')
else:
    print('Esse item não está na lista')
# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
# mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
# Euros.

nome = input('Digite o nome: ')
valor = float(input('Digite o valor em reais: '))

print(f"Valor em dólares: {round(valor / 4.87, 2)}")
print(f"Valor em euros: {round(valor / 5.27, 2)}")
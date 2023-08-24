# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
# mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
# Euros.

nome = input()
valor = float(input())

print(f"Valor em dólares: {valor / 4.87}")
print(f"Valor em euros: {valor / 5.27}")
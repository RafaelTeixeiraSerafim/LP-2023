# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
# de aumento.

preco = float(input('Digite o preço de um produto: '))

print(f"5% de desconto: {round(preco * 0.95, 2)}")
print(f"15% de aumento: {round(preco * 1.15, 2)}")
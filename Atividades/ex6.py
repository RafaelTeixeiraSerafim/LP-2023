# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
# comprar.

dinheiro = float(input('Digite quanto dinheiro você tem: '))
print(f"Você pode comprar {round(dinheiro / 5.41, 2)} dólar(es)")
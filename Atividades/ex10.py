# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) – 58.

altura = float(input('Digite sua altura: '))

print(f"Seu peso ideal é {round((72.7 * altura) - 58, 2)} kg")
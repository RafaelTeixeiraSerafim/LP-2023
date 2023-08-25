# Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7 ∗ h) − 58
# • Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input('Altura: '))
sexo = input('Sexo (m/f): ')

if sexo == 'm':
    print(f"Peso ideal: {(72.7 * altura) - 58}")
elif sexo == 'f':
    print(f"Peso ideal: {(62.1 * altura) - 44.7}")
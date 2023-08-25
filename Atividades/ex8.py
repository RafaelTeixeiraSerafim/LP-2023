# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
# quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = round(largura * altura, 2)

print(f"Área: {area}")
print(f"Litros de tinta: {area / 2}")
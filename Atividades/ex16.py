# Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
# para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
# conversão.

tipo = int(input('Escolha uma opção: \n1- Fahrenheit para Celsius\n2- Celsius para Fahrenheit\n'))
temp = float(input('Temperatura: '))

if tipo == 1:
    print(round((temp-32) / 1.8, 2))
else:
    print(round(temp * 1.8 + 32, 2))
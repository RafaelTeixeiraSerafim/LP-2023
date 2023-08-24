# Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
# tela dizendo se está “quente”, “frio” ou “agradável”.

temp = float(input('Temperatura Atual: '))

if temp < 20:
    print('Frio')
elif temp < 25:
    print('Agradável')
else:
    print('Quente')
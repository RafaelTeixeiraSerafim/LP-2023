# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
# ele.

s = input()

print(f"Alfanumérico: {s.isalnum()}")
print(f"Alfabético: {s.isalpha()}")
print(f"ASCII: {s.isascii()}")
print(f"Decimal: {s.isdecimal()}")
print(f"Digito: {s.isdigit()}")
print(f"Identificador Válido: {s.isidentifier()}")
print(f"Minúsculo: {s.islower()}")
print(f"Maiúsculo: {s.isupper()}")
print(f"Numérico: {s.isnumeric()}")
print(f"Printável: {s.isprintable()}")
print(f"Espaço: {s.isspace()}")
print(f"Título: {s.istitle()}")
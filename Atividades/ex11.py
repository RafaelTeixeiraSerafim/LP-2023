# Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
# trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
# ao final mostrar seu nome e salário final calculado.

nome = input('Digite seu nome: ')
horas = float(input('Digite o número de horas trabalhadas: '))
valor = float(input('Digite o valor da hora trabalhada: '))

salario_bruto = horas * valor

print(f"Salário bruto: {salario_bruto}")
print(f"{nome}, seu salário final é {salario_bruto * 0.98}")
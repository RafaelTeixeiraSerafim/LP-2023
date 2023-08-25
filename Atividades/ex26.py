# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Digite seu sexo (m/f): ')
estado_civil = input('Digite seu estado civil (s, c, v, d): ')

if len(nome) <= 3:
    print('\nSeu nome deve ter mais que três caracteres')

if idade < 0 or idade > 150:
    print('Sua idade deve ser entre 0 e 150')

if salario < 0:
    print('Seu salário deve ser maior que zero')

if sexo != 'm' and sexo != 'f':
    print('Seu sexo deve ser masculino ou feminino (meio homofóbico isso)')

if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Digite um estado civil válido')
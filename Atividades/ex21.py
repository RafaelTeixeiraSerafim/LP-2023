# Crie um programa que leia dois valores e mostre na tela um menu :
# a. Somar
# b. Multiplicar
# c. Maior
# d. Menor
# e. Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

while True:
    num1 = float(input("\nPrimeiro número: "))
    num2 = float(input("Segundo número: "))

    opcao = input('Escolha uma opção: \na. Somar \nb. Multiplicar \nc. Maior \nd. Menor \ne. Sair do programa \n')

    if opcao == 'a':
        print(num1 + num2)
    elif opcao == 'b':
        print(num1 * num2)
    elif opcao == 'c':
        print(max(num1, num2))
    elif opcao == 'd':
        print(min(num1, num2))
    elif opcao == 'e':
        break
    else:
        print('Opção inválida')

# Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
# Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
# a. Soma de 2 números.
# b. Diferença entre 2 números (maior pelo menor).
# c.Produto entre 2 números.
# d. Divisão entre 2 números (o denominador não pode ser zero).

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
opcao = input('Escolha uma opção: \na. Soma de 2 números. \nb. Diferença entre 2 números (maior pelo menor). \nc. Produto entre 2 números. \nd. Divisão entre 2 números (o denominador não pode ser zero). \n')

if opcao == 'a':
    print(num1 + num2)
elif opcao == 'b':
    print(max(num1, num2) - min(num1, num2))
elif opcao == 'c':
    print(num1 * num2)
elif opcao == 'd':
    if num2 == 0:
        print("Denominador não pode ser 0")
    else:
        print(num1 / num2)
else:
    print('Opção inválida')

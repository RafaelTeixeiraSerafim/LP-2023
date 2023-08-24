# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar.
# As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Idade: "))
tempo = int(input("Tempo de serviço em anos: "))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
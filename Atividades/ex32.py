# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
# obtidos os seguintes dados:
# a. Código da cidade; (digitado pelo usuário)
# b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
# c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
# Deseja-se saber:
# b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# c. Qual a média de veículos nas cinco cidades juntas;
# d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

codigos = []
veiculos = []
acidentes = []

for i in range(5):
    c = int(input('\nDigite o código da cidade: '))
    v = int(input('Digite o número de veículos de passeio (em 1999): '))
    a = int(input('Digite o número de acidentes de trânsito com vítimas (em 1999): '))

    codigos.append(c)
    veiculos.append(v)
    acidentes.append(a)

maior = 0
cid_maior = 0
menor = float('inf')
cid_menor = 0
soma_acid = 0
num_acid = 0

for i in range(5):
    if acidentes[i] > maior:
        maior = acidentes[i]
        cid_maior = codigos[i]
    
    if acidentes[i] < menor:
        menor = acidentes[i]
        cid_menor = codigos[i]
    
    if veiculos[i] < 2000:
        soma_acid += acidentes[i]
        num_acid += 1

media_acid = soma_acid / num_acid
media_veic = sum(veiculos) / 5

print(f'\nO menor índice de acidentes de trânsito é {menor} e pertence a cidade com código {cid_menor}')
print(f'O maior índice de acidentes de trânsito é {maior} e pertence a cidade com código {cid_maior}')
print(f'A média de veículos nas cinco cidades é {media_veic}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é {media_acid}')

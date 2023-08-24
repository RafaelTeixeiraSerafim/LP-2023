# Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
# peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
# aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

pri = float(input('Primeira nota (peso 5): '))
seg = float(input('Segunda nota (peso 5): '))
ter = float(input('Terceira nota (peso 10): '))

media = (pri + seg + ter) / 2

print(f'Sua média é {media}')

if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado')
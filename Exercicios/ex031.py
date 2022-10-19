#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
km = float(input('Digite a distância da viagem em Km'))
'''caro = km * 0.50
barato = km * 0.45
if km >= 200:
    print(f'O preço é R${barato}')
else:
    print(f'O preço é R${caro}')'''
if km>=200:
    preço = km * 0.45
else:
    preço = km * 0.50
print(f'O preço de sua passagem será de {preço}')

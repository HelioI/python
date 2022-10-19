# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoas = dict()
amontoado = list()
acima = list()
soma = média = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    amontoado.append(pessoas.copy())
    while True:
        continuar = str(input('Continuar: [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 50)
print(f'A) Ao todo temos {len(amontoado)} pessoas cadastradas.')
média = soma / len(amontoado)
print(f'B) A média de idade é {média:5.2f} anos.') # c
print('C) As mulheres cadastradas foram ', end='') # d
for p in amontoado:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Pessoas com idade acima da média: ', end='')
for p in amontoado:
    if p['Idade'] > média:
        print(f'{p["Nome"]} ', end='')
print()

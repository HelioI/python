#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
h = m20anos = p18 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        p18 += 1
    if sexo in 'M':
        h += 1
    if sexo in 'F' and idade < 20:
        m20anos += 1
    c += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'No total foram cadastrados:\n {p18} pessoas com mais de 18 anos\n {h} homens\n {m20anos} mulheres com menos de 20 anos.')

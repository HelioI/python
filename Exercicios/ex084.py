#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
galera = list()
dado = list()
maior = menor = 0
print('Pesos')
while True:
    pessoas = dado.append(str(input('Nome: ')))
    peso = dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = str(input('Continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in galera:
    if c[1] == maior:
        print(f'[{c[0]}]', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for c in galera:
    if c[1] == menor:
        print(f'[{c[0]}]', end='')
print()

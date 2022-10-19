#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    continuar = str(input('Continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')

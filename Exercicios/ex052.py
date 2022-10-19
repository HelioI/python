#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
contagem = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        contagem += 1
    else:
        print('\033[33m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {contagem} vezes.')
if contagem == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')

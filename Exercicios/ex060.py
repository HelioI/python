#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from time import sleep
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
sleep(2)
'''while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''
for c in range(n, 0, -1):
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
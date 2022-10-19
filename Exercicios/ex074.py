#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
ordem = sorted(tupla)
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
#print(f'O maior valor sorteado foi {ordem[4:5]}') FUNCIONA TAMBÉM
#print(f'O menor valor sorteado foi {ordem[0:1]}') FUNCIONA TAMBÉM
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')

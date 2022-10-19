# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []


def sorteia():
    for x in range(1, 6):
        num = randint(1, 10)
        numeros.append(num)
    print('Sorteando 5 valores inteiros: ', end=' ')
    for v in numeros:
        sleep(0.4)
        print(f'{v}', end=' ')


def somapar():
    somar = 0
    for v in numeros:
        if v % 2 == 0:
            somar += v
    print(f'\nSomandos os valores pares de {numeros}, temos {somar} ')


sorteia()
somapar()
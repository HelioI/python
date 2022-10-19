#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = list()
listajogos = list()
jogos = int(input('Quantos jogos serão sorteados?'))
total = 1
while total <= jogos:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    listajogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {jogos} jogos')
sleep(2)
for i, l in enumerate(listajogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')

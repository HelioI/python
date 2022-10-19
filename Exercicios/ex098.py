# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador():
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.7)
    print('\nContagem de 10 até 0 de 2 em 2:')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.7)
    print('\nAgora é sua vez:')
    início = int(input('Início:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {início} até {fim} indo de {passo} em {passo}:')
    if início < fim:
        for c in range(início, fim+1, passo):
            print(c, end=' ')
            sleep(0.7)
    elif início > fim:
        if passo > 0:
            for c in range(início, fim - 1, -passo):
                print(c, end=' ')
                sleep(0.7)
    if início == fim:
        print('Não existe contagem.')
    print()
    print('-='*30)
    print('{:>30}'.format('PROGRAMA ENCERRADO!'))


# PP
contador()
#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    escolha =int(input('''Escolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa'''))
    menu = escolha
    if menu == 1:
        print(f'O resultado da soma entre {n1} e {n2} é {n1 + n2}')
    elif menu == 2:
        print(f'O resultado da multiplicação entre {n1} e {n2} é {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f' O maior número é {n2}')
    elif menu == 4:
        n1 = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-=' * 20)
sleep(2)
print('Operação concluída!')

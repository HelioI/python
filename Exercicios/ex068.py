#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('Jogo do Par ou Ímpar')
from random import randint
v = 0
while True:
    while True:
        jogador = int(input('Digite um valor: '))
        computador = randint(0, 10)
        total = jogador + computador
        decide = ' '
        while decide not in 'PI':
            decide = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
        print('DEU Par' if total % 2 == 0 else 'DEU ÍMPAR')
        if decide == 'P':
            if total % 2 == 0:
                print('Você venceu!!')
                v += 1
            else:
                print('Você perdeu!')
                break
        if decide == 'I':
            if total % 2 == 1:
                print('Você venceu!!')
                v += 1
            else:
                print('Você perdeu!')
                break
    continuar = ' '
    while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Você venceu {v} vezes.')
print('GAME OVER')

#Escreva um program que faça o computador ''pensar'' em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o jogador venceu ou perdeu.
from random import randint
from time import sleep
jogador= int(input('Digite seu número'))
computador= randint(0,5)
print('PROCESSANDO...')
sleep(2)
print(f'O número era {computador}')
if jogador==computador:
    print('Você venceu!')
else:
    print('Você perdeu!')

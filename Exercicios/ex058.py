#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
print('Jogo da avinhação')
sleep(1)
print('Pensansdo em um número entre 0 e 10...')
sleep(5)
computador = randint(0, 10)
jogador = int(input('Tente adivinhar o número que pensei')) #acertou = false
tentativas = 1
while computador != jogador: #while not acertou:
    jogador = int(input('Não é esse número, tente mais uma vez!'))
    tentativas += 1
    if jogador < computador:
        print('Mais...')
    elif jogador > computador:
        print('Menos...')
print(f'O número que pensei era {computador}!')
print('Parabéns você acertou!')
print(f'Você levou {tentativas} tentativas para acertar!')
if tentativas == 1:
    print('De prima!')
elif tentativas <= 5:
    print('Mais ou menos')
else:
    print('Vish')

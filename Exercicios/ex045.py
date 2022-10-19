#Crie um programa que faça o computador jogar jokenpô com você.
from random import choice
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra, papel, tesoura]
jogador = str(input('Pedra, papel ou tesoura?')).strip().lower()
computador = (choice(lista))
print(f'Eu escolho {computador}')
if jogador == pedra and computador == tesoura:
    print('Você venceu!')
elif jogador == pedra and computador == papel:
    print('Você perdeu!')
elif jogador == tesoura and computador == papel:
    print('Você venceu!')
elif jogador == tesoura and computador == pedra:
    print('Você perdeu!')
elif jogador == papel and computador == pedra:
    print('Você venceu!')
elif jogador == papel and computador == tesoura:
    print('Você perdeu!')
elif jogador == computador:
    print('Empate!')
else:
    print('Jogada inválida.')
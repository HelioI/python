# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'J1': randint(0, 6),
        'J2': randint(0, 6),
        'J3': randint(0, 6),
        'J4': randint(0, 6)}
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print(f'Parabéns {ranking[0][0]}!')
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
futebol = dict()
partidas = list()
futebol['Nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input('Partidas jogadas: '))
for c in range(0, totalpartidas):
    partidas.append(int(input(f'Gols na partida {c+1}: ')))
futebol['Gols'] = partidas[:]
futebol['Totalgols'] = sum(partidas)
print(futebol)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {futebol["Nome"]} jogou {totalpartidas} partidas.')
for i, v in enumerate(partidas):
    print(f' ==> Na partida {i+1}, fez {v} gol(s).')
print(f'Foi um total de {futebol["Totalgols"]} gol(s)')

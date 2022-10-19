#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
futebol = dict()
partidas = list()
while True:
    futebol.clear()
    futebol['Nome'] = str(input('Nome do jogador: '))
    totalpartidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, totalpartidas):
        partidas.append(int(input(f'Gols na partida {c+1}: ')))
    futebol['Gols'] = partidas[:]
    futebol['Totalgols'] = sum(partidas)
    time.append(futebol.copy())
    while True:
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite S ou N!')
    if continuar == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in futebol.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    usuario = int(input('Qual jogador que ver os dados? (999 para encerrar) '))
    if usuario == 999:
        break
    if usuario >= len(time):
        print(f'Erro! Não existe jogador com código {usuario}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[usuario]["Nome"]}:')
        for i, g in enumerate(time[usuario]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

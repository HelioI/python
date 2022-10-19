#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Internacional.
b = ('Pa', 'Cor', 'Flu', 'Cap', 'Fla', 'Int', 'Cam', 'RB', 'San', 'Amg',
     'Sao', 'Bot', 'Go', 'Cea', 'Ctb', 'Ava', 'For',
     'Cui', 'Ago', 'Juv')
print('-x'*100)
print(f'Lista de times: {b}')
print('-x'*100)
print(f'G5{b[:5]}')
print('-x'*100)
print(f'Z4 {b[16:]}')
print('-x'*100)
print(f'Times em ordem alfabética: {sorted(b)}')
print('-x'*100)
print(f"O Internacional está na {b.index('Int')+1}° posição")
print('-x'*100)

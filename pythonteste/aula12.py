nome = str(input('Qual seu nom?'))
if nome == 'Hélio':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria':
    print('Que nome feio')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')

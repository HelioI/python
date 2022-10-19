# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
info = dict()
info['Nome'] = str(input('Nome: '))
info['Média'] = float(input(f'Média de {info["Nome"]}: '))
if info['Média'] < 5:
    info['Situação'] = 'Reprovado'
elif info['Média'] < 7:
    info['Situação'] = 'Recuperação'
else:
    info['Situação'] = 'Aprovado'
for k, v in info.items():
    print(f'{k} é igual a {v}')

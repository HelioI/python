#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
    continuar = str(input('Continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(lista)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(lista): # i == index == indice == NO. == Número
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if escolha == 999:
        print('FINALIZANDO...')
        break
    if escolha <= len(lista) - 1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
print('<<< VOLTE SEMPRE >>>')

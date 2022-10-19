#Um professor quer sortear um dos quatros alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
Aluno1 = input('Digite o nome do primeiro aluno')
Aluno2 = input('Digite o nome do segundo aluno')
Aluno3 = input('Digite o nome do terceiro aluno')
Aluno4 = input('Digite o nome do quarto aluno')
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
print(f'O escolhido foi {choice(lista)}')

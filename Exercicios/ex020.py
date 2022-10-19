#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = input('Nome do primeiro aluno')
a2 = input('Nome do segundo aluno')
a3 = input('Nome do terceiro aluno')
a4 = input('Nome do quarto aluno')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação será {lista} ')

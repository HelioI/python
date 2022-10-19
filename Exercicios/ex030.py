#Crie um programa que leia um número inteiro na tela e mostre se ele é PAR ou ÍMPAR.
n1 = float(input('Digite um número'))
resultado = n1 % 2
if resultado == 0:
    print('PAR.')
else:
    print('ÍMPAR.')

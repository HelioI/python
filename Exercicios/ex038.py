#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
valor1 = float(input('Qual o primeiro número?'))
valor2 = float(input('Qual o segundo número?'))
valor3 = float(input('Qual o terceiro número?'))
if valor1 > valor2 and valor3:
    print('O primeiro valor é maior.')
elif valor2 > valor1 and valor3:
    print('O segundo valor é maior.')
elif valor3 > valor1 and valor2:
    print('O terceiro valor é maior.')
elif valor1 == valor2 and valor3:
    print('Não existe valor maior, os três são iguais.')

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = float(input('Comprimento da primeira reta'))
reta2 = float(input('Comprimento da segunda reta'))
reta3 = float(input('Comprimento da terceira reta'))
combo1 = reta1+reta2
combo2 = reta1-reta2
if reta3 >= combo2 and combo1 >= reta3:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')

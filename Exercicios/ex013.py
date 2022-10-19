#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Digite o salário R$'))
novo = salário*15/100
print(f'O salário com aumento é R${salário+novo:.2f1}')

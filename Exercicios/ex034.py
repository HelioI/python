#Escreva um programa que calcule o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.
salário = float(input('Salário R$'))
superior = salário*(10/100)+salário
inferior = salário*(15/100)+salário
if salário <= 1250:
    print(f'O salário ficou:{inferior:.2f}')
else:
    print(f'O salário ficou:{superior}')
#Dá pra colocar dentro do if e else a variável também.
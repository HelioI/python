#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = 'sexo'
M = 'Masculino'
F = 'Feminino'
sexo = str(input('Sexo [M/F]')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo.\nSexo [M/F]')).strip().upper()
if sexo == 'M':
    print('Sexo Masculino registrado.')
elif sexo == 'F':
    print('Sexo Feminino registrado.')
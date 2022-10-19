#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo')).strip()
completo = nome.split()
print(completo[0])
print(completo[-1])

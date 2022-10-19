#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um número'))
b = int(input('Digite outro'))
c = int(input('Digite mais um'))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor é {menor} e o maior é {maior}.')

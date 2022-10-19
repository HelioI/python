#Faça um programa que leia um ano qualquer e mostre se ele é um BISSEXTO.
from datetime import date
ano = int(input('Digite um ano'))
bissexto = ano%4
#if ano == 0: ESSE COMANDO NÃO ESTÁ FUNCIONANDO CORRETAMENTE.
   # ano = date.today().year
if bissexto == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

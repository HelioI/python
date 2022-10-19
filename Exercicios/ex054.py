#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    pessoa = int(input(f'Em que ano a {c}° pesssoa nasceu? '))
    atual = date.today().year
    idade = atual - pessoa
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoa(s) maior(es) de idade.')
print(f'E também tivemos {menor} pessoa(s) menor(es) de idade. ')

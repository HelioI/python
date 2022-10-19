#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor é {maior} nas posições: ', end='')
for pos, c in enumerate(valores):
    if c == maior:
        print(f'{pos}', end=' ')
print(f'\nO menor valor é {menor} nas posições: ', end='')
for pos, c in enumerate(valores):
    if c == menor:
        print(f'{pos}', end=' ')
'''lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')
'''
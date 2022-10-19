#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = 'S'
soma = quantidade = média = menor = maior = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma += número
    quantidade += 1
    if quantidade == 1:
        menor = maior = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / quantidade
print(f'Você digitou {quantidade} e a média foi {média}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')

#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
c = total = produtos1000 = barato = 0
nomebarato = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto?R$ '))
    total += preço
    if preço > 1000:
        produtos1000 += 1
    if c == 1 or preço < barato:
        barato = preço
        nomebarato = nome #Não ta funcionando
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'No total foi gasto R${total:.2f}')
print(f'Temos {produtos1000} produtos custando mais de R$1000')
print(f'O produto mais barato é {nomebarato}, custando {barato}')
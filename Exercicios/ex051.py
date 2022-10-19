#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão?'))
décimo = primeiro + (10-1) * razão
print('Progressão Aritmética')
for c in range(primeiro, décimo + razão, razão):
    print(c, end=' > ')
print('ACABOU')

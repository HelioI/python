#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão?'))
termo = primeiro
contagem = 1
print('Progressão Aritmética')
while contagem <= 10:
    print(f'{termo} > ', end='')
    termo += razão
    contagem += 1
print('FIM')

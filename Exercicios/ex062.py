#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão?'))
termo = primeiro
contagem = 1
total = 0
mais = 10
print('Progressão Aritmética')
while mais !=0:
    total += mais
    while contagem <= total:
        print(f'{termo} > ', end='')
        termo += razão
        contagem += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados;')
print('FIM')
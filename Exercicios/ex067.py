#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    '''if c <= 10:
        print(f'{valor} x {c:2} = {valor*c}')'''
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('Programa encerrado.')

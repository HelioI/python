#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
''''inicio = 0
tabuada = int(input('Tabuada do número:'))
fim = 11 * tabuada
contador = -1
for c in range(inicio, fim, tabuada):
    contador += 1
    print(f'{contador} x {c}')'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')


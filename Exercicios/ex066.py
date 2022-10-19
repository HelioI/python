#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
s = c = 0 #Não precisa colocar a variável 'valor' nesse caso, quando for while True
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma foi {s}!')

#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = contagem = soma = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar]'))
    if n != 999:
        contagem += 1
        soma += n
print(f'Você digitou {contagem} números e a soma foi {soma}')

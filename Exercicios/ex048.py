#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
#pra otimizar processamento range(3, 500, 6) ou então range(3, 496, 7)
for c in range(1, 501, 2):
    if c % 3 == 0:
        #acumulador soma um valor e o contador conta
        contador = contador + 1
        soma = soma + c
print(f'A soma de todos os {contador} valortes solicitados é {soma}')
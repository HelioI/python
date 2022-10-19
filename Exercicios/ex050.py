#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contagem = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
        contagem += 1
print(f'Você informou {contagem} número(s) PAR(ES) e a soma foi {soma}')
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* valores):
    contagem = omaior = 0
    print('-=' * 50)
    for num in valores:
        print(num, end=' ')
        if contagem == 0:
            omaior = num
        else:
            if num > omaior:
                omaior = num
        contagem += 1
    print(f'\nForam informados {contagem} valores ao todo.')
    print(f'O maior valor é {omaior}.')


# PP
maior(1, 5, 2, 4)
maior(1, 2)
maior(0)
maior(-1, -2, 2, 5)
maior()

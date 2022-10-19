# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    resultado = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {resultado}m².')


# PP
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m) '))
area(largura, comprimento)

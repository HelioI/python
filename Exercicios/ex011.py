#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
h = float(input('Digite a altura'))
b = float(input('Digite a largura'))
p = h*b
print(f'Para pintar a área de {h*b}metros será necessário {p/2}litros de tinta')

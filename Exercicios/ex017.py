#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o cumprimento da hipotenusa.
'''from math import sqrt
Coposto = float(input('Quanto mede o cateto oposto'))
Cadjacente = float(input('Quanto mede o cateto adjacente'))
Hipotenusa = sqrt(Coposto**2 + Cadjacente**2)
print(f'A hipotenusa vai medir {Hipotenusa:.2f}')'''

from math import hypot
Coposto = float(input('Quanto mede o cateto oposto'))
Cadjacente = float(input('Quanto mede o cateto adjacente'))
Hipotenusa = hypot(Coposto, Cadjacente)
print(f'A hipotenusa vai medir {Hipotenusa:.2f}')

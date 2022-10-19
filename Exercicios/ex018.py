#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
Angulo = float(input('Qual é o ângulo'))
Cos = cos(radians(Angulo))
Sen = sin(radians(Angulo))
Tan = tan(radians(Angulo))
print(f'O ângulo de {Angulo} tem o SENO de {Sen:.2f}')
print(f'O ângulo de {Angulo} tem o COSSENO de {Cos:.2f}')
print(f'O ângulo de {Angulo} tem a TANGENTE de {Tan:.2f}')

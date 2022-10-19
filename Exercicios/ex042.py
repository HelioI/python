#Refaça o DESAFIO 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero:todos os lados iguais -Isósceles:dois lados iguais -Escaleno:todos os lados diferentes
reta1 = float(input('Primeiro segmento'))
reta2 = float(input('Segundo segmento'))
reta3 = float(input('Terceiro segmento'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um ', end='')
    if reta1 == reta2 == reta3:
        print('Triângulo Equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Triângulo Isósceles')
    elif reta1 != reta2 != reta3 != reta1:
        print('Triângulo Escaleno')
    #else:
else:
    print('Os segmentos acima não podem formar um triângulo.')
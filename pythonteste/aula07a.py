n1 =int(input('Digite um valor: '))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.4f} ',end='>>')
print(f'Divisão inteira {di} Resto da divisão {rd} e potência {e}')

nome = input('Qual é seu nome')
print(f'Prazer em te conhecer{nome *5}!')
print(f'Olá,{nome:.^50}'.lower())
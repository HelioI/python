# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
vn = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in vn:
        vn.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não irei adicionar.')
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
vn.sort()
print(vn)

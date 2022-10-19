#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40)
lista = ('Lápis', 1.15, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)
'''print(f"{lista[0]} {('-'*20)} R${lista[1]:.2f}")
print(f"{lista[2]} {('-'*20)} R${lista[3]:.2f}")
print(f"{lista[4]} {('-'*20)} R${lista[5]:.2f}")
print('-'*40)'''
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)

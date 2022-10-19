#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.
preço = float(input('Digite o preço do produto'))
novo = preço*5/100
print(f'Com 5% de desconto o preço fica: {preço-novo:.2f}')

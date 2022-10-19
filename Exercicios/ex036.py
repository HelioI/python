#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa?'))
salário = float(input('Qual é seu salário?'))
anos = float(input('Em quantos anos será pago'))
meses = anos*12
porcento = salário*(30/100)
parcela = casa/meses
print(f'O valor da parcela é {parcela:.2f}')
if parcela > porcento:
    print('Como o valor da parcela supera 30% do seu salário não é possível efetuar o empréstimo.')
else:
    print('É possível efetuar o empréstimo.')
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço norma e condição de pagamento:
#-À vista dinheiro/cheque:10% de desconto -À vista no cartão:5% de desconto -Em até 2x no cartão:preço normal -3x ou mais no cartão:20% de juros
print(f'{"Lojas Teste":=^40}')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço*(10 / 100))
elif opção == 2:
    total = preço - (preço*(5/100))
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço*(20/100))
    parctotal = int(input('Quantas parcelas?'))
    parcela = total / parctotal
    print(f'Sua compra será parcelada em {parctotal}x de R${parcela:.2f} COM JUROS')
else:
    print('Opção inválida. Tente novamente.')
    total = preço
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')

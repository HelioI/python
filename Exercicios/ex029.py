#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km= float(input('Digite a velocidade em Km'))
multa = (km-80) * 7
if km > 80:
    print(f'Você foi multado em:R${multa:.2f}')
else:
    print('Você não foi multado.')
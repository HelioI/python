#Desenvolva uma lógica que leia o peso a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5:Abaixo do peso -Entre 18.5 e 25:Peso ideal -25 até 30:Sobrepeso -30 até 40:Obesidade -Acima de 40:Obesidade mórbida
altura = float(input('Altura (M) : '))
peso = float(input('Peso (Kg) : '))
imc = peso / (altura*altura)

#if altura.is_integer():
    #altura = altura / 100           Tenho que testar isso ainda.

print(f'Seu imc é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 25 > imc >= 18.5:
    print('Peso ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 >= imc >= 30:
    print('Obesidade')
elif imc >40:
    print('Obesidade mórbida')

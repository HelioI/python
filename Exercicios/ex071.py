usuario = str(input('Digite o usuário: '))
saque = int(input('Digite o valor a ser sacado: '))
total = saque
cedulas = 50
totalcedulas = 0
print(f'Olá, {usuario}!')
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        print(f'Total de {totalcedulas} cédulas de R${cedulas:.0f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break

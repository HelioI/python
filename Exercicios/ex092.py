#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
carteira = dict()
carteira['Nome'] = str(input('Nome: '))
carteira['Idade'] = int(input('Ano de nascimento: '))
idade = date.today().year - carteira['Idade']
carteira['Idade'] = idade
carteira['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if carteira['ctps'] == 0:
    for k, v in carteira.items():
        print(f'{k}: {v}')
else:
    carteira['Contratação'] = int(input('Ano de contratação: '))
    carteira['Salário'] = float(input('Salário: R$ '))
    carteira['Aposentadoria'] = carteira['Contratação'] + carteira['Idade'] + 35 - date.today().year
    print(carteira)
    for k, v in carteira.items():
        print(f'{k}: {v}')

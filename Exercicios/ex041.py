#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
#-Até 9 anos:Mirim -Até 14 anos:Infantil -Até 19 anos:Junior -Até 20 anos:Sênior -Acima:Master
from datetime import date
atual = date.today().year
nasceu = int(input('Digite o ano de nascimento'))
idade = atual - nasceu
print(f'O atleta tem {idade} ano(s).')
if idade > 25:
    print('Master')
elif idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai alistar ao serviço militar. -Se é a hora de se alistar. -Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasceu = int(input('Ano de nascimento'))
idade = atual - nasceu
print('Sexo:Masculino/Feminino')
sexo = str(input('[M]\n[F}')).strip().upper()
if sexo == 'F':
    print('Não é necessário fazer alistamento obrigatório.')
else:
    print(f'Quem nasceu em {nasceu} tem {idade} anos em {atual}.')
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade > 18:
        saldo = idade - 18
        alistar = atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {alistar}.')
    elif idade < 18:
        saldo = 18 - idade
        alistar = atual + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {alistar}.')
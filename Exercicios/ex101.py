# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade >= 65 or 16 <= idade < 18:
        return print(f'Com {idade} anos: Voto opcional')
    elif idade >= 18:
        return print(f'Com {idade} anos: Voto obrigatório')
    else:
        return print(f'Com {idade} anos: Não vota')


# PP
voto(int(input('Em que ano você nasceu? ')))

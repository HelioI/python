def metade(n=0, formato=False):
    n /= 2
    return n if not formato else moeda(n)


def dobro(n=0, formato=False):
    n *= 2
    return n if not formato else moeda(n)       # pode usar esse


def aumentar(n=0, porc=0, formato=False):
    n += (n * (porc / 100))
    return n if formato is False else moeda(n)  # ou esse


def reduzir(n=0, porc=0, formato=False):
    n -= (n * (porc / 100))
    return n if formato is False else moeda(n)


def moeda(n=0, moedinha='R$'):
    formatado = f'{moedinha}{n:>.2f}'.replace('.', ',')
    return formatado


def resumo(n=0, aumento=10, reduçao=5):
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('-' * 50)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{reduçao}% de aumento: \t{reduzir(n, reduçao, True)}')
    print(f'{aumento}% de redução: \t{aumentar(n, aumento, True)}')

    print('-' * 50)

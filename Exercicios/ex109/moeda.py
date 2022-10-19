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

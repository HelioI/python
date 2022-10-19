def metade(n):
    n /= 2
    return n


def dobro(n):
    n *= 2
    return n


def aumentar(n, porc):
    n += (n * (porc / 100))
    return n


def reduzir(n, porc):
    n -= (n * (porc / 100))
    return n

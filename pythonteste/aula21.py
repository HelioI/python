def contador(i, f, p):
    """— > Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Hélio Ignácio
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    """
    s = a + b + c
    print(f'As soma vale: {s}')
    return s


def funcao():
    global n1
    n1 = 4 # local
    print(f'N1 dentro vale {n1}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
# PP
'''somar(c=3, a=2)
somar()
help(somar)'''


'''n1 = 2 # global
funcao()
print(f'N1 fora vale {n1}')'''


'''resp1 = (somar(1, 2, 5))
resp2 = somar(1)
resp3 = somar()
print(f'Meus cálculos deram {resp1}, {resp2} e {resp3}.')'''


'''f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1} {f2} {f3} ')'''


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
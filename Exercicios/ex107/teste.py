from ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 15% temos {moeda.moeda(moeda.reduzir(p, 15))}')

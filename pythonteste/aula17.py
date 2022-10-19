'''''n = [2, 5, 9, 1]
n.sort(reverse=True)
print(n)
n[2] = 4
n.append(7)
n.sort()
print(n)
n.insert(1, 2)
n.remove(4)
if 6 in n:
    n.remove(6)
else:
    print('Não achei o número 6')
n.pop()
print(f'Essa lista tem {len(n)} elementos.')
print(n)'''
#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista.')'''
#valores.append(5)
#valores.append(9)
#valores.append(4)
#print(valores)'''
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A{a}')
print(f'Lista B{b}')

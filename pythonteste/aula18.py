#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][1])
#for pessoa in galera:
#    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
galera = list()
dado = list()
maior = menor = 0
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'No total temos {maior} maior de idade e {menor} menor de idade.')

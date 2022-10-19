#pessoas = {'nome': 'Hélio', 'sexo': 'M', 'idade': 20}
#print(f" O {pessoas['nome']} tem {pessoas['idade']} anos.")
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Maicon' # substitui
#pessoas['peso'] = 70.8  # adiciona
#for k, v in pessoas.items(): # para cada k(keys), v(values) em pessoas.item()
#    print(f'{k} = {v}')  # vai mostrar isso

'''brasil = list()
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3): #para cada c(contagem) no alcance(0,3): 0, 1, 2.
    estado['uf'] = str(input('Unidade federativa: ')) #faça um loop disso naquele alcance.
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
#print(brasil)
for e in brasil:
#   for k, v in e.items():
#        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()  #pula linha
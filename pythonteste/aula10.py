#Condição
'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')'''

#Condição simplificada
'''tempo = int(input('Quanto anos tem seu carro?'))
print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')'''

#Condição Composta
'''nome = str(input('Qual é seu nome'))
if nome == 'Hélio':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
print(f'A sua média foi {m:.2f}')
if m <=4.99:
    print('Você não foi aprovado')
else:
    print('Parabéns você foi aprovado')
if m>=6:
    print('Aprovado')
else:
    print('Reprovado')

#Simplificada abaixo
#print(f'PARABÉNS' if m >=6 else 'ESTUDE MAIS')
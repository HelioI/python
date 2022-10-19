#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridade = 0
homemvelho =''
mulherjovem = 0
for c in range(1, 5):
    print(f'----{c}° PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':   #usa o in pra não precisar dar .upper.()
        maioridade = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherjovem += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho tem {maioridade} anos e se chama {homemvelho}.')
print(f'Ao todo são {mulherjovem} mulheres com menos de 20 anos.')

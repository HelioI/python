#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in lista:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end= ' ')

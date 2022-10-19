#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
abre = list()
fecha = list()
frase = str(input('Digite uma expressão que use parênteses: '))
for simbolo in frase:
    if simbolo == '(':
        abre.append('(')
    elif simbolo == ')':
        fecha.append(')')
if len(abre) == len(fecha):
    print('Sua expressão está correta.')
elif len(abre) != len(fecha):
    print('Sua expressão está errada.')

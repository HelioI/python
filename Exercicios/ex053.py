#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '''''#solução usando for
inverso = junto[::-1] #solução usando fatiamento
'''for letra in range(len(junto) - 1, -1, -1): #Isso vai caçar as letras equivalentes a contagem que aparece se tirar.
    inverso += junto[letra]'''#Solução usando for
print(f'O inverso de {frase} é {inverso}.')
if junto == inverso:
    print(f'{frase} é um palíndromo.')
else:
    print(f'{frase} não é um palíndromo.')

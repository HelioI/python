#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#frase = str(input('Digite sua frase')).strip().upper()
#frase2 = frase.replace(('Á , A')).replace(('Â, A'))
#print(f"A letra 'A' apareceu {frase.count('A')} vezes no texto. A primeira letra A está na casa {frase2.find('A')} e a última na casa {frase2.rfind('A')}.")

frase = str(input('Digite uma frase: ')).strip().upper()
frase2 = frase.replace('Á', 'A').replace('Â','A')
print(f"A letra 'A' apareceu {frase.count('A')} vezes no texto. A primeira letra A está na casa {frase2.find('A')} e o última na casa {frase2.rfind('A')}.")




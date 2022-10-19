#Crie um programa que leia duas notas de uma aluno e calcule sua média, mostrando no final, de acordo com a média atinigida:
#-Média abaixo de 5.0:REPROVADO -Média entre 5 e 6.9:RECUPERAÇÃO -Média 7.0 ou superior:Aprovado
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
média = (n1+n2)/2
if média < 5.0:
    print(f'Sua média foi {média:.1f}\nReprovado')
elif média >= 7.0:
    print(f'Sua média foi {média:.1f}\nAprovado')
elif média >= 5 and média < 7:
#elif 7 > média >= 5:
#else:
    print(f'Sua média foi {média:.1f}\nRecuperação')

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.
n1 = float(input('Digite um número'))
print(f'É equivalente a {n1*100:.0f} centímetros e {n1*1000:.0f} milímetros')
print(f' {n1/1000}km\n {n1/100}hm\n {n1/10}dam\n {n1*10:.0f}dm\n {n1*100:.0f}cm\n {n1*1000:.0f}mm')
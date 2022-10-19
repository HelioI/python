# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(texto):
    riscos = len(texto) + 4
    print('-' * riscos)
    print(f'  {texto}')
    print('-' * riscos)


# PP
escreva(str(input('Digite uma mensagem: ')))

# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n


def leiafloat(texto):
    while True:
        try:
            n = float(input(texto))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n


numreal = leiaint('Digite um Real: ')
numinteiro = leiafloat('Digite um Inteiro: ')
print(f'Os valor inteiro digitado foi {numreal} e o inteiro {numinteiro}.')

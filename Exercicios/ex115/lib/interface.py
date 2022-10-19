def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n


def linha(tamanho=42):
    return '-' * tamanho


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc

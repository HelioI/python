# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
c = ('\033[m',         # 0 - sem cores
     '\033[0;97;41m',  # 1 - vermelho
     '\033[0;97;42m',  # 2 - verde
     '\033[0;97;43m',  # 3 - amareo
     '\033[0;97;44m',  # 4 - azul
     '\033[0;97.45m',  # 5 - roxo
     '\033[7;107m'     # 6 - branco
     )


def ajuda(comando):
    titulo(f'Acessando o manual do comando\'{comando}\'',  4)
    print(c[6], end='')
    help(comando)


def titulo(texto, cor=0):
    tamanho = len(texto) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)
    print(c[0], end='')


# PP
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        help(comando)
titulo('ATÉ LOGO!', 1)

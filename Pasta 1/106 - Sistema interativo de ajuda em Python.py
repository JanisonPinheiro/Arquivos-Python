print('Exercício Python #106 - Sistema interativo de ajuda em Python')

c = ('\033[m',  # 0 - sem cor
     '\033[7;30m',  # 1 - branco
     '\033[1;30;41m',  # 2 - vermelho
     '\033[1;30;42m',  # 3 - verde
     '\033[1;30;43m',  # 4 - amarelo
     '\033[1;30;44m',  # 5 - roxo
     '\033[1;30:45m',  # 6 - cinza
     '\033[1;30;46m',  # 7 - magenta
     '\033[1:30;47m',  # 8 - cinza
     )


def ajuda(con):
    titulo(f'Acessando o manual do comando\'{con}\'', 4)
    help(con)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE COMANDO PyHELP', 3)
    comando = str(input('Função ou Biblioteca. '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)

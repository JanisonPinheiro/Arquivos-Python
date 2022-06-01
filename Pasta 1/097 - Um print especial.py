def lin():
    print('\033[34m=\033[m' * 42)


lin()
print('Exercício Python #097 - Um print especial')
lin()


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


escreva('Janíson Pinheiro')
escreva('Olá')

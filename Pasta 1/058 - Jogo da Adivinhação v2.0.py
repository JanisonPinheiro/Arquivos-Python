print('\033[34m-' * 48)
print('Exercício Python #058 - Jogo da Adivinhação v2.0')
print('-' * 48)
from random import randint
computador = randint(0, 10)
print('\033[mSou seu computador... Acabei de pensar em um número entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais alto, tente de novo')
        else:
            print('Mais baixo,tente de novo')
print('Acertou com {} tentativas'.format(palpites))

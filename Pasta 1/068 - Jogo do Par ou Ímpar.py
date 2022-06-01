print('\033[34m=+' * 22)
print('Exercício Python #068 - Jogo do Par ou Ímpar')
print('=+' * 22)
from random import randint
vitoria = 0
while True:
    jogador = int(input('\033[mDigite um número:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            vitoria += 1
        else:
            print('\033[31mVocê PERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            vitoria += 1
        else:
            print('\033[31mVocê PERDEU\033[m')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes')

print('{:=^90}'.format('Exercício Python #045 - GAME: Pedra Papel e Tesoura'))
import random
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
lista = [0, 1, 2]
sorteado = random.choice(lista)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
if jogada >= 3:
    print('NÃO TEM ESSA OPÇÃO KARALHO')
elif jogada == sorteado:
    print('EMPATOU, eu também escolhi {}'.format(itens[sorteado]))
elif jogada != sorteado:
    if jogada == 0 and sorteado == 1:
        print('Eu ganhei, escolhi PAPEL.')
    if jogada == 0 and sorteado == 2:
        print('Você ganhou, eu escolhi TESOURA.')
    if jogada == 1 and sorteado == 0:
        print('Você ganhou, eu escolhi PEDRA.')
    if jogada == 1 and sorteado == 2:
        print('Eu ganhei, escolhi TESOURA')
    if jogada == 2 and sorteado == 0:
        print('Eu ganhei, escolhi PEDRA')
    if jogada == 2 and sorteado == 1:
        print('Você ganhou, eu escolhi PAPEL.')

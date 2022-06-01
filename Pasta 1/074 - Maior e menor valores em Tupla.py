print('\033[34m=' * 54)
print('Exercício Python #074 - Maior e menor valores em Tupla')
print('=' * 54)
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10), randint(0, 10),)
print('\033[mOs valores sorteados foram')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}'
      f'\nO menor valor sorteado foi {min(num)}')


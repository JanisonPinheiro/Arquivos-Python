print('\033[34m-' * 43)
print('Exercício Python #054 - Grupo da Maioridade')
print('-' * 43)
from datetime import date
dataatual = date.today().year
tot = 0
tot1 = 0
for c in range(1, 8):
    data = int(input('\033[mDigite a {}° ano de nasimento: '.format(c)))
    if dataatual - data >= 21:
        tot += 1
    else:
        tot1 += 1
print('{} Pessoas já antigiram a maioridade. '.format(tot))
print('{} Pessoas ainda não antingiram a maioridade. '.format(tot1))


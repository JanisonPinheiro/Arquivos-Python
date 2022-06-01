print('\033[34m{:*^80}\033[m'.format('Exercício Python #046 - Contagem regressiva'))
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM')

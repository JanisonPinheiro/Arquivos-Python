print('\033[34m-' * 43)
print('Exercício Python #060 - Cálculo do Fatorial')
print('-' * 43)
num = int(input('\033[mDigite um número para calcular seu Fatorial: '))
c = num
f = 1
print(f'Calculando {num}! =', end=' ')
while c > 0:
    print(f'{c}  ', end='')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')

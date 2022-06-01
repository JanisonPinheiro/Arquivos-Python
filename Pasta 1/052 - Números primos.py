print('\033[34m=' * 38)
print('Exercício Python #052 - Números primos')
print('=' * 38)
num = int(input('\033[mDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso não é primo.')

print('{:_^80}'.format('Exercício Python #049 - Tabuada v.2.0'))
n = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))

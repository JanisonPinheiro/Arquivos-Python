print('=' * 36)
print('Exercício Python #067 - Tabuada v3.0')
print('=' * 36)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 33)
    for c in range(1, 11):
        print(f'{n} x {c}  = {n * c}')
    print('-' * 33)
print('Programa encerrado')


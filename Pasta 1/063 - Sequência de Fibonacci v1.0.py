print('\033[34m-' * 51)
print('Exercício Python #063 - Sequência de Fibonacci v1.0')
print('-' * 51)
num = int(input('\033[mQuantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3# contador de termos
while cont <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')

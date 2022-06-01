print('\033[34m=' * 38)
print('Exercício Python #050 - Soma dos pares')
print('\033[34m=\033[m' * 38)
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares, a soma deles equivale a {}'.format(cont, soma))
 
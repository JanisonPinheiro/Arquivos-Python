print('\033[34m-' * 50)
print('Exercício Python #061 - Progressão Aritmética v2.0')
print('-' * 50)
print('\033[mGerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    cont += 1
print('Fim')



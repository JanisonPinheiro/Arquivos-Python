print('=' * 51)
print('Exercício Python #079 - Valores únicos em uma Lista')
print('=' * 51)
numeros = list()
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou {numeros}')

print('\033[34m=^' * 24)
print('Exercício Python #066 - Vários números com flag')
print('=^' * 24)
digitados = soma = 0
while True:
    num = int(input('\033[mDigite um número [999 para parar]: '))
    if num == 999:
        break
    digitados += 1
    soma += num
print(f'Números digitados {digitados}, o resultado da soma entre eles é {soma}')

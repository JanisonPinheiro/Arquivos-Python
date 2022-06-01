print('Exercício Python #082 - Dividindo valores em várias listas')
lnum = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lnum.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont in 'Nn':
        break
print(f'A lista completa {lnum}'
      f'\nA lista de Pares {par}'
      f'\nA lista de Ímpares {impar}')


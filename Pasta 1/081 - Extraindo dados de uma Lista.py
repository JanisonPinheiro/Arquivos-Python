print('Exercício Python #081 - Extraindo dados de uma Lista')
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi digitado')
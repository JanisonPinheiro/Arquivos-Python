from random import randint
from time import sleep
print('Exercício Python #100 - Funções para sortear e somar')


def sorteia(lista):
    print('Sorteando os números.', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        sleep(0.3)
        print(f'{n}', end=' ')
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)

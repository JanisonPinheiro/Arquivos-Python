from time import sleep
print('Exercício Python #099 - Função que descobre o maior')


def maior(*num):
    print('-' * 33)
    if len(num) == 0:
        print('Analisando os valores passados...'
              '\nForam informados 0 valores ao todo.'
              '\nO maior valor informado foi 0.')
    else:
        print(f'Analisando os valores passados...')
        for valor in num:
            print(f'{valor} ', end=' ')
        print(f'Foram informados {len(num)} valores ao todo.'
              f'\nO maior valor informado foi {max(num)} ')
        sleep(1.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(87, 87, 5, 6)

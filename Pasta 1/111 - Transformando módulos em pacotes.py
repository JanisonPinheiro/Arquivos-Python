print('Exercício Python #111 - Transformando módulos em pacotes')
from des111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)

moeda

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(preço)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print('-' * 30)
    print(f'Metade do preço: \t{metade(preço, True)}')
    print('-' * 30)
    print(f'Com {taxaa}% de aumento:\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)

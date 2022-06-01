print('Exercício Python #102 - Função para Fatorial')


def factorial(n, show=False):
    """
       Calcula o fatorial no numero
       :param n: numero a calculo o fatorial inteiro
       :param show: Mostra a cada passo da conta (opcional)
       :return: resultado do fatorial
       """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x', end=' ')
            else:
                print(' = ', end='')
        f *= c
    return f


print(factorial(5, show=True))

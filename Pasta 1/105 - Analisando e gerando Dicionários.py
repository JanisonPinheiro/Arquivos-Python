print('Exercício Python #105 - Analisando e gerando Dicionários')


def notas(*n, sit=False):
    """
   Função para analizar notas de um ou mais alunos e dizer sua situação.
    :param n: uma ou mais nota(s) de aluno(s) para ser analizador.
    :param sit: (Opcional) adiciona a situação do aluno com base na média das notas.
    :return: retorna um dicionário com a maxima, minima e a média das notas informadas
     e a situação do aluno(caso sit=True).
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)

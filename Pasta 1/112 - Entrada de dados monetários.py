print('Exercício Python #112 - Entrada de dados monetários')

from des112.utilidadescev import moeda
from des112.utilidadescev import dados
p = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: {entrada} é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

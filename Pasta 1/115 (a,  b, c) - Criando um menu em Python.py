sistema.py

from des115.lib.intface import *
from des115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

print('Exercício Python #115 (a,  b, c) - Criando um menu em Python')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        """Opção de listar o conteúdo de um arquivo"""
        lerArquivo(arq)
    elif resposta == 2:
        """Opção de cadastrar uma nova pessoa"""
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaint('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema.')
        break
    else:
        print('\033[31mErro! DIGITE UM NÚMERO VÁLIDO\033[m')
    sleep(2)

__init__.py


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            break
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}')
        c += 1
    print(linha())
    opc = leiaint('\033[36mSua Opção: \033[m')
    return opc


arquiv.py

from des115.lib.intface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ')
        else:
            print(f'Novo resgistro de {nome} adicionado.')
            a.close()


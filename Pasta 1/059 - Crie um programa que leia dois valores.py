print('\033[34m-'*85)
print('Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela')
print('\033[34m-\033[m'*85)
from time import  sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a opção? '))
    if opcao == 1:
        print('A soma dos números escolhidos é {}'.format(num1 + num2))
    elif opcao == 2:
        print('O valor multiplicado entre {} e {} é {} '.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número é {} '.format(num1))
        else:
            print('O maior número digitado é {} '.format(num2))
    elif opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida')
        print('Tente novamente.')
    print('\033[31m-=\033[m' * 10)
    sleep(2)
print('FIM DO PROGRAMA VOLTE SEMPRE.')

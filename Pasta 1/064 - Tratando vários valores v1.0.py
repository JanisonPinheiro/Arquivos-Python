print('\033[34m=' * 52)
print('Exercício Python #064 - Tratando vários valores v1.0')
print('=' * 52)
num = cont = soma = 0
num = int(input('\033[mDigite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

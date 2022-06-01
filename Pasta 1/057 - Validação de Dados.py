print('\033[34m-' * 42)
print('Exercício Python #057 - Validação de Dados')
print('-' * 42)
sexo = str(input('\033[mDigite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

print('\033[34m-' * 50)
print('\033[33mExercício Python #042 - Analisando Triângulos v2.0')
print('\033[34m-\033[m' * 50)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTRO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não forma um triângulo.')

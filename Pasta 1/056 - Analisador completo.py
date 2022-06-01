print('Exercício Python #056 - Analisador completo')
mas = 0
fem = 0
idade = 0
media = 0
velho = 0 #Saber quem é o mais velho
for c in range(1, 5):
    print('-----{}° PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F] ')).strip()
    media += idade / 4 #A média de idade entre os 4
    if sexo in 'Mn':
        mas += 1  # Saber quantos do sexo masculino tem
        if idade > velho:
            velho = idade
            maisvelho = nome
    elif sexo in 'Ff':
        if idade < 20: # Saber quantas pessoas do sexo feminino tem menos que 20 anos
            fem +=1 #Se tiver menos que 20 SOMA 1
print('A média de idade entre eles é {:.0f} anos'.format(media))
print('Ao todo são {} pessoas do sexo feminino com MENOS de 20 anos'.format(fem))
if mas == 0:
    print('Não tem nehuma pessoa do sexo Masculino')
elif mas >= 1:
    print('O homem mais velho é {} e tem {} anos '.format(maisvelho, velho))

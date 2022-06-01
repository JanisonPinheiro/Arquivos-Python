print('Exercício Python #101 - Funções para votação')


def voto(x):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'COM {idade}: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO.'


ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))

import urllib
import urllib.request
print('Exercício Python #114 - Site está acessível?')
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessivél no momento')
else:
    print('Conseguir acessar o site Pudim com sucesso')

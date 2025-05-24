'''
Como encurtar URLs em Python
O pacote pyshorteners permite fazer isso de forma fácil e rápida


Baixar o pip instal pyshorteners no cmd
'''

import pyshorteners

#Entrando com uma URL  que será encurtada
url = "https://guilhermedosantoss.github.io/Portfolio/"

#Iniciando o objeto para encurtamento de URLs
link = pyshorteners.Shortener()

# Realizando o encurtamento da URL
url_encurtada = link.tinyurl.short(url)

print(f'\n{shorten_url}')
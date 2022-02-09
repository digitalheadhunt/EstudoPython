import re
import os
import requests
from bs4 import BeatifulSoup


url = input("Digite uma url: ")

#Pegar uma url e acessar ela remotamente

http = requests.get(url)

#Dar uma parse para html com o bs4

response = BeatifulSoup(http.text, "html.parser")

#usar um regex para separar as imagens do restante do html
regex = re.compile("/src\s*=\s*"(.+?)"/")
count = 0
matches = []

with open("lista_imgs.txt","a") as listas:
	for line in response:
		


#Salvar as tags das imagens num novo arquivo de texto

#iterar nesse novo arquivo de texto para acessar as imgs

#usar o os para dar uma curl e baixar as imagens do arquivo

#salvar essas imagens numa pasta



import re
import os
import requests
from bs4 import BeatifulSoup


url = input("www.google.com")

#Pegar uma url e acessar ela remotamente

http = requests.get(url)

#Dar uma parse para html com o bs4

response = BeatifulSoup(http.text, "html.parser")

#usar um regex para separar as imagens do restante do html
count = 0
matches = []

# with open("lista_imgs.txt","a") as listas:
# 	for line in response:
		
import re
import requests
from bs4 import BeautifulSoup

url = input("Digite a url: ")

http = requests.get(url)

doc = BeautifulSoup(http.text, "html.parser")

imgs = doc.find_all("img")

num = 0
for i in imgs:
	print(i['src'])
	num +1
	file_name = "img"+num+".jpg"
	response = requests.get(i['src'])
	file = open(file_name,"wb")
 	file.write(response.content)
	file.close()

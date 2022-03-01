import requests
from bs4 import BeautifulSoup
import re

url = ""

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

title = doc.find_all(text=re.compile("[r R]+_\w+"))

element = []

for e in title:
	element = (e.strip())

print(element)



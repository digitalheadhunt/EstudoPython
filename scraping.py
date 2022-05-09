# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url = "www.eos.com"

page = urlopen(url)

print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('div', {"class": "story-body sp-story-body gel-body-copy"})

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text
print(article)

# Saving the scraped text
with open('scraped_text.txt', 'w') as file:
    file.write(article)

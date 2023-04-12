from bs4 import BeautifulSoup
import requests

url = 'https://commons.wikimedia.org/wiki/Rhododendron'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

imgs = soup.find_all('a', class_="image")

links = []
for img in imgs:
    # print(dir(img))
    row_list = str(img).split(" ")
    link = ''
    for el in row_list:
        if el.startswith("src="):
            link = el
            links.append(link)

for l in links:
    print(l)
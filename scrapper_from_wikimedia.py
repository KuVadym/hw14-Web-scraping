# from bs4 import BeautifulSoup
# import requests

# url = 'https://commons.wikimedia.org/wiki/Rhododendron'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# imgs = soup.find_all('a', class_="image")

# links = []
# for img in imgs:
#     # print(dir(img))
#     row_list = str(img).split(" ")
#     link = ''
#     for el in row_list:
#         if el.startswith("src="):
#             link = el
#             links.append(link)

# for l in links:
#     print(l)

my_div_str = "div, div, div"


div_list = []
def div_parser(div):
    
    if div.find_all("div"):
        div = el.find_all("div")
        div_parser(div)
        return div
    else: 
        return div_list.append(div)
    
div_parser(my_div_str)
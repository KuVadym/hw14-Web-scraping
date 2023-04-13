from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


# url = "https://academy.cs.cmu.edu/docs/canvas"
url = "https://academy.cs.cmu.edu/docs/generalShapeProperties"
driver = webdriver.Chrome(r"c:\path\to\chromedriver.exe")
driver.get(url)

sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

page = soup.find("div", class_="docs-article content")
page = page.find("div")
result = ''


div_list = []
def div_parser(div):
    global div_list

    for el in div:
        if el.find_all("div", class_="inline_editor", recursive=False):
            div_list.append(el)    

        elif el.find_all("div"):
            div = el.find_all("div", recursive=False)
            div_parser(div)

        else: 
            div_list.append(el)


div_parser(page)


# for el in div_list:
#     code = ''
    # text = ''
    # if el.find_all("div", class_="ace_line"):
    #     for div in el:
    #         if not div.find_all("div", class_="ace_gutter-cell"):
    #             text = div.text
    #         code = div.find_all("div", class_="ace_layer ace_text-layer")
    # else:
    # if not el.find_all("div", class_="ace_gutter-cell"):
    #     text = el.text

    # if code:
    #     for el in code:
    #         result += el.text
    #         result += "\n"
    #     result += "\n"

    # if text:
    #     result += text
    #     result += "\n"


for el in page:    
    code = el.find_all("div", class_="ace_line")
    img_scription = el.find_all("div", class_="docs-image-notes")
    head = el.find_all("h3")
    text = el.find_all("p")

    if img_scription:
        for el in img_scription:
            result += el.text
            result += "\n"

    if head:
        for el in head:
            result += el.text
            result += "\n"
    if code:
        for el in code:
            result += el.text
            result += "\n"
        result += "\n"

    
    if text:
        for el in text:
            result += el.text
            result += "\n"
    



print(result)

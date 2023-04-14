from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


# url = "https://academy.cs.cmu.edu/docs/canvas"
url = "https://academy.cs.cmu.edu/docs/generalShapeProperties"
driver = webdriver.Chrome(r"c:\path\to\chromedriver.exe")
driver.get(url)
div_list = []
sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

title = soup.find("div", class_="docs-article-title")
div_list.append(title)
page = soup.find("div", class_="docs-article content")
page = page.find("div")
result = ''



def div_parser(div):
    global div_list

    for el in div:
        if el.has_attr('class') and el["class"][0] == "docs-intro-example":  
            for _ in el:
                if not _.find_all("div", class_="ace_line"):
                    div_list.append(_)

                elif _.find_all("div", class_="ace_line"):       
                    div_list.append(_)  
 

        elif el.find_all("div"):
            div = el.find_all("div", recursive=False)
            div_parser(div)

        else: 
            div_list.append(el)


div_parser(page)
for el in div_list:    
    code = el.find_all("div", class_="ace_line")
    text = el.find_all("p")

    if code:
        for el in code:
            result += el.text
            result += "\n"
        result += "\n"
    
    else:
        result += el.text
    

print(result)

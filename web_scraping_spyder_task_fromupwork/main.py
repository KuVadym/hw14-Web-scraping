from time import sleep
from bs4 import BeautifulSoup, element
from selenium import webdriver
from parsers import link_parser

# url = "https://academy.cs.cmu.edu/docs/canvas"
url = "https://academy.cs.cmu.edu/docs/docs"
driver = webdriver.Chrome(r"c:\path\to\chromedriver.exe")
driver.get(url)
pages_for_parsing = link_parser()


result = ''
div_list = []
# pages = []


def div_parser(div:element.Tag | element.NavigableString) -> None:
    '''
    !!! Attention !!!
    
    If you call this func, you have to create a variable "div_list".
    It should be empty list.

    result will be on that list


    This func get page or its part and.
    First element is div with class "ace_line"
    Second element is other div that do not includ other divs elements.
    '''

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


for parsing_page in pages_for_parsing:
    print(parsing_page)
    driver.get(parsing_page)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    title = soup.find("div", class_="docs-article-title")
    result += title.text
    page = soup.find("div", class_="docs-article content")

    # page = page.find("div")


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

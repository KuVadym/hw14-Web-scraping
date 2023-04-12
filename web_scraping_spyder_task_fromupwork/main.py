from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://academy.cs.cmu.edu/docs/canvas"
driver = webdriver.Chrome(r"c:\path\to\chromedriver.exe")
driver.get(url)

sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

page = soup.find("div", class_="docs-article content")
page = page.find("div")
result = ''
print(len(page))
for el in page:

    code = el.find_all("div", class_="ace_line")
    text = el.find_all("p")
    
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

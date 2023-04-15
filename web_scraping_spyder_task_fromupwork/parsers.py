from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup


url = "https://academy.cs.cmu.edu/docs"
driver = webdriver.Chrome(r"C:\Users\ktuzik\Desktop\scraping\hw14-Web-scraping\web_scraping_spyder_task_fromupwork\chromedriver.exe")
driver.get(url)

pages = []


# sleep(5)
def link_parser() -> list:
    '''
    If you call this func, you have to create a variable "pages".
    It should be empty list.

    This function is open click on all buttons and it is started JS scripts.
    After that it returns all links in left side bar.
    '''
    global pages
    try:
        # find tab/button
        osiButton = driver.find_elements(By.CLASS_NAME, 'sidebar-parent')
        for el in osiButton:
            # print('button text: ' + el.text)
            if el not in pages: 
                # print('click on: ' + el.text)
                el.click()
                pages.append(el)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        bar = soup.find_all("span", class_="indicator closed")
        # print(bar)
        if bar:
            link_parser()
        
        # print(" links")
        raw_links = soup.find_all("a", class_="docs-link")
        links = []
        for link in raw_links:
            # print(link.text)
            links.append("https://academy.cs.cmu.edu" + link["href"])

        return links

    except Exception as ex:
        print(ex)

# ready_links_list = link_parser()
# print(ready_links_list)




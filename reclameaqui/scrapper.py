from requests import Session
from bs4 import BeautifulSoup

url = 'https://www.reclameaqui.com.br/empresa'
    # фейковый заголовок, чтобы не раскрываться что мы - бот
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def scraping(headers):
    links = []

        # используем сессию, чтобы автоматически работать с куками
    work = Session()
    response = work.get('https://www.reclameaqui.com.br/empresa/claro/lista-reclamacoes/', headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        page = soup.find_all('div', class_='sc-1pe7b5t-0 iQGzPh')
        pages = soup.find_all('div', class_='sc-1sm4sxr-3 fGiCjJ')


        # Count pages range
        for el in pages:    
            if el.text.find('…'):
                last_page = el.text[el.text.find('…')+1:]
        
        for page in range(1, 2): # last_page
            response = work.get(f'https://www.reclameaqui.com.br/empresa/claro/lista-reclamacoes/?pagina={page}', headers=headers)
            if response.status_code == 200:
                print(f'Get links from page: {page}')
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                parsing_pages = soup.find_all('div', class_='sc-1pe7b5t-0 iQGzPh')
                # el.findall('li', class_='sc-lgQHWK kqOZOU')

                for article in parsing_pages:
                    # print(article)
                    # title = article.find_all('h4', class_='sc-1pe7b5t-1 jAlTVn')
                    links_on_page = article.find_all('a')

                    for el in links_on_page:
                        link = el.get('href')
                        links.append(url + link)
    print(len(links))
    return links
          

urls = scraping(headers)

def getting_data(headers, url):
    work = Session()
    response = work.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # print(soup)
        review_title = soup.find_all('h1')
        review_text = soup.find_all('p')
        city = soup.find_all('div', class_='lzlu7c-6 lzlu7c-7 bOKpGx xfMNV')
        date = soup.find_all('div', class_='lzlu7c-6 lzlu7c-8 bOKpGx cVmIra')
        review_id = soup.find_all('div', class_='lzlu7c-6 lzlu7c-9 bOKpGx fumsuP')

        print(f'title: {review_title}')
        print(f'text: {review_text}')
        print(f'city: {city}')
        print(f'date: {date}')
        print(f'id: {review_id}')


for url in urls:
    print(url)
    getting_data(headers, url)
    break
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from unicodedata import name
from itemadapter import ItemAdapter
import sqlite3
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import literal
from .spiders.model import Quote, Base, Tag, Autors, AutorsInfo
import requests
from bs4 import BeautifulSoup
import lxml.html


  
  
class ScrapytutorialPipeline(object):
    def __init__(self):
        self.create_conn()
  
    # create connection method to create database
    # or use database to store scraped data
    def create_conn(self):

        self.engine = create_engine("sqlite:///qoutes_and_authors.db")
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
   
    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item
  
    def putitemsintable(self, item):
        tags = item.get('keywords')
        keywords_list = []
        for tag in tags:
            check = self.session.query(Tag).filter(Tag.name == str(tag))
            if self.session.query(literal(True)).filter(check.exists()).scalar() == True:
                keywords_list.append(self.session.query(Tag).filter(Tag.name == str(tag)).first())
            else:
                keyword=Tag(name=str(tag))
                keywords_list.append(keyword)

        check = self.session.query(Autors).filter(Autors.name == str(item.get('author')))
        if self.session.query(literal(True)).filter(check.exists()).scalar() == True:
            author = self.session.query(Autors).filter(Autors.name == str(item.get('author'))).first()
        else:
            author = Autors(name=str(item.get('author')), description_linc=str(item.get('link')))
            response = requests.get(str(item.get('link')))
            soup = BeautifulSoup(response.text, "lxml")
            name = soup.find(class_="author-title").get_text(strip=True)
            birthdate = soup.find(class_="author-born-date").get_text(strip=True)
            birthplace = soup.find(class_="author-born-location").get_text(strip=True)
            descripson = soup.find(class_="author-description").get_text(strip=True)
            author_info = AutorsInfo(name=name, birthdate=birthdate, birthplace=birthplace, description=descripson, author_info=author)
        check_quote = self.session.query(Quote).filter(Quote.name == str(item.get('quote')))
        if self.session.query(literal(True)).filter(check_quote.exists()).scalar() == True:
            pass
        else:   
            self.quote = Quote(name=item.get('quote'), author=author)
            self.quote.tags = keywords_list
            self.session.add(self.quote)
            self.session.commit()
        self.session.close()



# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy




class ExportToDB(scrapy.Item):
    keywords = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()
    link = scrapy.Field()